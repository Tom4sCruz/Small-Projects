#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>

// Vertex Shader source code
const char* vertexShaderSource = R"(
    #version 330 core
    layout (location = 0) in vec3 aPos;
    void main() {
       gl_Position = vec4(aPos, 1.0);
    }
)";

// Fragment Shader source code
const char* fragmentShaderSource = R"(
    #version 330 core
    out vec4 FragColor;
    void main() {
       FragColor = vec4(1.0, 0.5, 0.2, 1.0);
    }
)";

int main() {
    // Initialize GLFW
    if (!glfwInit()) {
        std::cerr << "Failed to initialize GLFW" << std::endl;
        return -1;
    }
    
    // Configure GLFW: set OpenGL version to 3.3, use core profile
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    
    // Create a window
    GLFWwindow* window = glfwCreateWindow(800, 600, "OpenGL Triangle", nullptr, nullptr);
    if (!window) {
        std::cerr << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    
    // Load OpenGL function pointers using GLAD
    if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress)) {
        std::cerr << "Failed to initialize GLAD" << std::endl;
        return -1;
    }
    
    // Build and compile the shader program
    // Vertex Shader
    unsigned int vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, nullptr);
    glCompileShader(vertexShader);
    // (Error checking omitted for brevity)
    
    // Fragment Shader
    unsigned int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, nullptr);
    glCompileShader(fragmentShader);
    // (Error checking omitted for brevity)
    
    // Link shaders to create a shader program
    unsigned int shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);
    // (Error checking omitted for brevity)
    
    // Clean up shaders (no longer needed once linked)
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);
    
    // Set up vertex data (a triangle) and buffers and configure vertex attributes
    float vertices[] = {
        -0.5f, -0.5f, 0.0f, // left vertex
         0.5f, -0.5f, 0.0f, // right vertex
         0.0f,  0.5f, 0.0f  // top vertex
    };
    
    unsigned int VBO, VAO;
    glGenVertexArrays(1, &VAO);  // Generate VAO
    glGenBuffers(1, &VBO);       // Generate VBO
    
    // Bind the VAO
    glBindVertexArray(VAO);
    
    // Bind and set VBO data
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    
    // Specify how OpenGL should interpret vertex data
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    
    // Unbind the VAO (optional)
    glBindVertexArray(0);
    
    // Render loop
    while (!glfwWindowShouldClose(window)) {
        // Process input (e.g., close on pressing Escape)
        if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
            glfwSetWindowShouldClose(window, true);
        
        // Clear the screen
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);
        
        // Draw the triangle
        glUseProgram(shaderProgram);
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 3);
        
        // Swap buffers and poll IO events
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    
    // Clean up allocated resources
    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glfwTerminate();
    
    return 0;
}

