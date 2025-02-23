import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js'
// init
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setAnimationLoop(animate);
document.body.appendChild(renderer.domElement);

// Daws the Axis
const axesHelper = new THREE.AxesHelper(1);
scene.add(axesHelper);

// Draws Cube
const cube_geometry = new THREE.BoxGeometry( 1, 1, 1 );
const cube_material = new THREE.MeshBasicMaterial({color: 0x00ff00});
const cube = new THREE.Mesh(cube_geometry, cube_material);

cube.position.set(0,1,0);

scene.add(cube);

// Draws Edges of the Cube
const edges = new THREE.EdgesGeometry(cube_geometry);
const edgeMaterial = new THREE.LineBasicMaterial({color: 0xff0000});
const wireframe = new THREE.LineSegments(edges, edgeMaterial);

wireframe.position.set(0,1,0);

scene.add(wireframe);

// Draws Plane
const plane_geometry = new THREE.PlaneGeometry(5,5);
const plane_material = new THREE.MeshBasicMaterial({color: 0x111111});
const plane = new THREE.Mesh (plane_geometry, plane_material);

plane.rotation.x = - Math.PI / 2;

scene.add(plane);

// Camera position
camera.position.set(3,2,5);
const controls = new OrbitControls(camera, renderer.domElement);
controls.target.copy(cube.position);


function animate() {
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    wireframe.rotation.x += 0.01;
    wireframe.rotation.y += 0.01;

    controls.update();

	renderer.render( scene, camera );
}
