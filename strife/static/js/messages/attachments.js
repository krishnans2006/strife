$(document).ready(() => {
    const uploadButton = $('#upload-attachment')[0];
    const fileStorage = $('#attachments')[0];
    const fileDisplay = $('#attachments-view');

    // When the upload button is clicked
    uploadButton.addEventListener('click', () => {
        const canUploadAttachments = $(this).data('can-upload-attachments');
        if (!canUploadAttachments) {
            return;
        }
        fileStorage.click();
    });

    // When a file is uploaded
    fileStorage.addEventListener('change', () => {
        console.log(fileStorage.files);

        // Update the list of files
        for (let i = 0; i < fileStorage.files.length; i++) {
            const file = fileStorage.files[i];
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
                  <a href="${url}" target="_blank" class="inline-block min-w-20 py-1 px-2.5 rounded-xl bg-gray-700 text-white cursor-pointer mb-2">
                      ${file.name}
                  </a>
              `);
        });
    });
});
