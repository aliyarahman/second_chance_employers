package org.mission_launch.returningcitzen;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.*;

public class RatingActivity extends Activity
{
	private Button submitButton;
	private RatingBar rating;
	private EditText companyName, description;
	private CheckBox askedBox, hiredBox;

	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_rating);
		submitButton = (Button) findViewById(R.id.submitButton);
		askedBox = (CheckBox) findViewById(R.id.askedCheck);
		hiredBox = (CheckBox) findViewById(R.id.hiredCheck);
		companyName = (EditText) findViewById(R.id.companyText);
		description = (EditText) findViewById(R.id.descriptionText);
		rating = (RatingBar) findViewById(R.id.ratingBar1);
		
		setupListeners();
	}
	
	private void setupListeners()
	{
		submitButton.setOnClickListener(new View.OnClickListener()
		{
			
			@Override
			public void onClick(View v)
			{
				boolean asked = askedBox.isChecked();
				boolean hired = hiredBox.isChecked();
				
			}
		});
	}
}
