using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using ContosoUniversity.DAL;
using ContosoUniversity.Models;
using System.Data.Entity.Infrastructure;

namespace ContosoUniversity.Controllers

{
    public class PolyController : Controller
    {
        private SchoolContext db = new SchoolContext();

        // GET: Poly
        public ActionResult Index()
        {
           Course c = db.Courses.Find(2);
            
            return View(c);
        }
        public String Result()
        {
            Course c = db.Courses.Find(2);

            return "{\"SortAs\": \"SGML\"}";
        }
    }
}