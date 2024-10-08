// When the upload button is clicked
$('#upload-attachment').on('click', function () {
    const canUploadAttachments = $(this).data('can-send-attachments');
    if (!canUploadAttachments) {
        return;
    }
    fileStorage.click();
})

const fileStorage = $('#attachments');
const fileDisplay = $('#attachments-view');

// When a file is uploaded
fileStorage.on('change', function () {
    console.log(fileStorage[0].files);

    // Update the list of files
    for (let i = 0; i < fileStorage[0].files.length; i++) {
        const file = fileStorage[0].files[i];
        const fileIndex = uploadedFiles.findIndex((f) => f.name === file.name);

        if (fileIndex === -1) {
            uploadedFiles.push(file);
        } else {
            uploadedFiles.splice(fileIndex, 1);
            uploadedFiles.push(file);
        }
    }

    // Update the file display
    fileDisplay.empty();
    uploadedFiles.forEach((file) => {
        const url = URL.createObjectURL(file);
        fileDisplay.append(`
                  <a href="${url}" target="_blank" class="inline-block py-1 px-2.5 rounded-xl bg-gray-700 text-white cursor-pointer mb-2">
                      ${file.name}
                  </a>
              `);
    });
});
