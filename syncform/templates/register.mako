<section>
    <div class="container">
      <div class="row">
        <form accept-charset="utf-8" action="${request.route_url('Registration_Action',%20action='submit')}" autocomplete="off" class="form-horizontal" enctype="multipart/form-data" id="validateForm" method="post" name="validateForm">
          <input class="col-sm-12 col-md-12 form-control" id="task" name="task" required="" type="hidden" value="${view}">

          <div class="form-row row form-group">
            <label class="control-label col-sm-3 col-md-3">Email
            Address</label>
            <div class="controls col-sm-9 col-md-9">
              <input class="row form-control" id="email" name="email" required="" type="email" value="${user.getEmail()}">
            </div>
          </div>

          <div class="form-row row form-group">
            <label class="control-label col-sm-3 col-md-3" for="mask-phone">Phone <span class="help-block">(999) 999-9999</span></label>
            <div class="controls col-sm-9 col-md-9">
              <input class="row form-control" id="mask-phone" name="phone" required="" tabindex="3" type="text">
            </div>
          </div>

          <div class="form-row row form-group">
            <label class="control-label col-sm-3 col-md-3">Address</label>
            <div class="controls col-sm-9 col-md-9">
              <input class="col-sm-12 col-md-12 form-control" id="street_address" name="street_address" required="" type="text" value="${user.getAddress()}">
            </div>
          </div>

          <div class="form-row row form-group">
            <label class="control-label col-sm-3 col-md-3">City</label>
            <div class="controls col-sm-9 col-md-9">
              <input class="col-sm-12 col-md-12 form-control" id="city" name="city" required="" type="text" value="${user.getCity()}">
            </div>
          </div>

          <div class="form-row row form-group">
            <label class="control-label col-sm-3 col-md-3">State</label>
            <div class="controls col-sm-9 col-md-9">
              <input class="col-sm-12 col-md-12 form-control" id="state" name="state" required="" type="text" value="${user.getState()}">
            </div>
          </div>

          <div class="form-row row form-group">
            <label class="control-label col-sm-3 col-md-3">Zip Code</label>
            <div class="controls col-sm-9 col-md-9">
              <input class="row form-control" id="zip_code" name="zip_code" required="" type="text" value="${user.getZipcode()}">
            </div>
          </div>

          <div class="form-row row form-group">
            <label class="control-label col-sm-3 col-md-3">Profile Image</label>
            <div class="controls col-sm-9 col-md-9">
              <div class="input-append row">
                <input class="col-sm-6 col-md-6 fileinput form-control" id="profile_image" name="profile_image" type="file">
              </div>
            </div>
          </div>

          <div class="form-row row form-group">
            <label class="control-label col-sm-3 col-md-3" for="elastic-textarea">About</label>
            <div class="controls col-sm-9 col-md-9">
              <textarea class="autogrow row" id="elastic-textarea" name="about" placeholder="Write a little bit about yourself" rows="5">${user.getAbout()}</textarea>
            </div>
          </div>

          <div class="form-actions row">
            <div class="col-lg-offset-3 col-sm-7 col-md-7">
              <button class="btn btn-primary" type="submit">Submit</button>
              <button class="btn btn-secondary btn-default" type="button">Cancel</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>