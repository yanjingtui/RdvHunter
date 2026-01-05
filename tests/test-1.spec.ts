import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://rdv-etrangers-94.interieur.gouv.fr/eAppointmentpref94/element/jsp/specific/pref94.jsp');
  await page.getByPlaceholder('Code Postal').click();
  await page.getByPlaceholder('Code Postal').fill('94110');
  await page.getByRole('button', { name: 'Continuer' }).click();
  await page.getByRole('checkbox').nth(2).check();
  await page.getByRole('button', { name: 'Continuer' }).click();
});
