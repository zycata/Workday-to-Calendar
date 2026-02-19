function Excel_Form() {
    const handleSubmit = async (e) => {
        e.preventDefault();

        const fileInput = e.target.elements.file; // 'file' matches the 'name' attribute on your input
        if (!fileInput.files[0]) return alert("Please select a file first");
        let file_name = fileInput.files[0].name
        if (!file_name.endsWIth(".xlsx")) return alert("Please upload an excel file");
        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        try {
            // 3. Send the POST request
            const response = await fetch("http://127.0.0.1:5100/convert-ics", {
                method: "POST",
                body: formData, 
            });

            const result = await response.json();
            console.log("Success:", result);
        } catch (error) {
            console.error("Error:", error);
        }
    };
    return (
        <form id="uploadForm" onSubmit={handleSubmit}>
            <input id="fileInput" type="file" name="file" />
            <button type="submit">Submit File</button>
        </form>
    );
}
