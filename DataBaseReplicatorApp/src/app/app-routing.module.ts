import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
// canActivate: [AuthGuard]
/*
FIXME: Tiene que estar primero el path de login y luego la raiz.
*/

/**
 * {
        path: 'login',
        loadChildren: './login/login.module#LoginModule'
    },
 */
const routes: Routes = [
    {
        path: 'main',
        loadChildren: './main/main.module#MainModule',
    },
    {
        path: 'login',
        loadChildren: './login.module#LoginModule'
    }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {}
