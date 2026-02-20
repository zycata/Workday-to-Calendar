function Excel_Form() {
    const handleSubmit = async (e) => {
        e.preventDefault();

        const fileInput = e.target.elements.file; // 'file' matches the 'name' attribute on your input
        if (!fileInput.files[0]) return alert("Please select a file first");
        let file_name = fileInput.files[0].name;
        if (!file_name.endsWith(".xlsx"))
            return alert("Please upload an excel file (.xlsx)");
        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        try {
            // 3. Send the POST request
            const response = await fetch("http://127.0.0.1:5100/convert-ics", {
                method: "POST",
                body: formData,
            });
            if (response.ok) {
                const result = await response.blob();
                const url = window.URL.createObjectURL(result);
                const a = document.createElement("a");
                a.href = url;
                a.download = "my_schedule.ics"; 
                document.body.appendChild(a);
                a.click(); 
                a.remove(); 
                window.URL.revokeObjectURL(url); 
            } else {
                const errorText = await response.text();
                alert("Error: " + errorText);
            }
        } catch (error) {
            console.error("Error:", error);
            alert("An error occured");
        }
    };
    return (
        <form id="uploadForm" onSubmit={handleSubmit}>
            <input id="fileInput" type="file" name="file" />
            <button type="submit">Convert File</button>
        </form>
    );
}

export default Excel_Form;
