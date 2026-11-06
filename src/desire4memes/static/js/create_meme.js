let canvas = null;

document.addEventListener("DOMContentLoaded", () => {
    canvas = new fabric.Canvas("meme");
    document.getElementsByClassName("canvas-container")[0].classList.add("mx-auto");

    document.getElementById("add_meme_background").addEventListener("change", add_meme_background);
    document.getElementById("add_rect").addEventListener("click", add_rect);
    document.getElementById("add_ellipse").addEventListener("click", add_ellipse);
    document.getElementById("add_textbox").addEventListener("click", add_textbox);
    document.getElementById("delete").addEventListener("click", delete_active_element);

    resizeCanvas(canvas);
    window.addEventListener("resize", () => {resizeCanvas(canvas)});
});

function resizeCanvas(myCanvas) {
    const width = window.innerWidth/1.5;
    const height = (9 * width) / 16;

    myCanvas.setDimensions({
        width: width,
        height: height
    });
    myCanvas.renderAll();
}

function add_meme_background(e) {
    const meme_background = e.target.files[0];
    if (!meme_background) return;

    const file_url = URL.createObjectURL(meme_background);

    fabric.FabricImage.fromURL(file_url).then(function(img) {
        img.set({
            scaleX: canvas.width / img.width,
            scaleY: canvas.height / img.height,
            left: canvas.width / 2,
            top: canvas.height / 2,
            selectable: false
        });
        
        canvas.backgroundImage = img;
        canvas.renderAll();
    
        URL.revokeObjectURL(file_url);
    }).catch(function(err) {
        console.error("Error loading uploaded image:", err);
        URL.revokeObjectURL(file_url);
    });
}

function add_rect() {
    const rect = new fabric.Rect({
        left: 100,
        top: 100,
        fill: "red",
        width: 60,
        height: 60
    });

    canvas.add(rect);
}

function add_ellipse() {
    const ellipse = new fabric.Ellipse({
        rx: 80,
        ry: 40,
        left: 100,
        top: 100,
        fill: "blue"
    });

    canvas.add(ellipse);
}

function add_textbox() {
    const textbox = new fabric.Textbox("Edit Me", {
        width: 400,
        fontSize: 24,
        left: 300,
        top: 300,
        fontFamily: "Impact",
        fill: "#333333",
        textAlign: 'left'
    });

    canvas.add(textbox);
}

function delete_active_element() {
    const active_object = canvas.getActiveObject()
    
    if (active_object) {
        canvas.remove(active_object)
    }
}