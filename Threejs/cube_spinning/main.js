import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js'
// init
const scene = new THREE.Scene();
const pers_camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
pers_camera.position.set(3,2,5);

const aspect = window.innerWidth / window.innerHeight;
const frustumSize = 10; // Controls the size of the view (higher = more zoomed out)

const ortho_camera = new THREE.OrthographicCamera(
    -frustumSize * aspect / 2,  // left
    frustumSize * aspect / 2,   // right
    frustumSize / 2,            // top
    -frustumSize / 2,           // bottom
    0.1,                        // near plane
    1000                        // far plane
);
ortho_camera.position.set(3,2,5);

// ACTIVE CAMERA
let activeCamera = pers_camera;

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setAnimationLoop(animate);
document.body.appendChild(renderer.domElement);

// Daws the Axis
const axesHelper = new THREE.AxesHelper(1);
scene.add(axesHelper);

// Draws light
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 10, 5);
light.castShadow = true;
scene.add(light);

// Draws Cube
const cube_geometry = new THREE.BoxGeometry( 1, 1, 1 );
var cube_material = new THREE.MeshStandardMaterial({color: 0x00ff00, transparent: true, opacity: 1});
const cube = new THREE.Mesh(cube_geometry, cube_material);

cube.position.set(0,1,0);

scene.add(cube);

// Draws Edges of Cube (Child of Cube)
const edges = new THREE.EdgesGeometry(cube_geometry);
const edgeMaterial = new THREE.LineBasicMaterial({color: 0xff0000});
const wireframe = new THREE.LineSegments(edges, edgeMaterial);

cube.add(wireframe);

// Draws Plane
const plane_geometry = new THREE.PlaneGeometry(5,5);
const plane_material = new THREE.MeshStandardMaterial({color: 0x111111, side: THREE.DoubleSide});
const plane = new THREE.Mesh (plane_geometry, plane_material);

plane.rotation.x = - Math.PI / 2;

scene.add(plane);

// Camera position
const pers_controls = new OrbitControls(pers_camera, renderer.domElement);
pers_controls.target.copy(cube.position);

const ortho_controls = new OrbitControls(ortho_camera, renderer.domElement);
ortho_controls.target.copy(cube.position);

// GUI
const cameraInput = document.getElementById("cameras");
const colorInput = document.getElementById("color");
const sizeInput = document.getElementById("size");
const heightInput = document.getElementById("height");
const transparencyInput = document.getElementById("transparency");
const wireframeInput = document.getElementById("wireframe");


// EVENT LISTENERS

window.addEventListener("keydown", (event) => {
    if (event.code === 'Space') {
        light.castShadow = !light.castShadow;
    }
    if (event.code === '1') {
    }
});

cameraInput.addEventListener("input", (event) => {
    const selectedCamera = event.target.value;
    if (selectedCamera === "pers") {
        activeCamera = pers_camera;
    } else {
        activeCamera = ortho_camera;
    }
});

colorInput.addEventListener("input", (event) => {
    cube.material.color.set(event.target.value);
});

sizeInput.addEventListener("input", (event) => {
    const selectedSize = event.target.value;
    cube.scale.set(selectedSize, selectedSize ,selectedSize);
});

heightInput.addEventListener("input", (event) => {
    cube.position.y = event.target.value;
});

transparencyInput.addEventListener("input", () => {
    if (transparencyInput.checked) {
        cube.material.opacity = 0.5;

    } else {
        cube.material.opacity = 1;
    }
});

wireframeInput.addEventListener("input", () => {
    if (wireframeInput.checked) {
        wireframe.visible = true;
    } else {
        wireframe.visible = false;
    }
});


function animate() {
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    pers_controls.update();
    ortho_controls.update();

	renderer.render( scene, activeCamera );
}




