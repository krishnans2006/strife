$(document).ready(() => {
    let currentRoleID = null;
    $(".role-expansion-trigger").on("click", function() {
        const roleID = $(this).data("role-id");
        if (currentRoleID === roleID) {
            currentRoleID = null;
            $(`#role-${roleID}`).hide();
        } else {
            if (currentRoleID !== null) {
                $(`#role-${currentRoleID}`).hide();
            }
            currentRoleID = roleID;
            $(`#role-${roleID}`).show();
        }
    });
});
