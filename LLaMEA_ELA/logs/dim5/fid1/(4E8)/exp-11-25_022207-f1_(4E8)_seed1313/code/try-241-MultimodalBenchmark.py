import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis with chaotic modulation and dynamic scaling
        radial = np.sum(np.exp(-2 * (x_norm**2).sum()) * 
                       np.cos(7 * np.pi * x_norm.sum()) * 
                       np.sin(3 * np.pi * x_norm.sum()) * 
                       (1 + 0.4 * np.sin(11 * np.pi * x_norm.sum())))
        
        # Modified sinusoidal component with fractal-like frequency variations and adaptive scaling
        sin_mod = np.sum(np.sin(5 * np.pi * x_norm) * 
                        np.cos(9 * np.pi * x_norm) * 
                        (1 + 0.6 * np.sin(13 * np.pi * x_norm)) * 
                        np.exp(-0.3 * np.abs(x_norm)) * 
                        (1 + 0.2 * np.cos(17 * np.pi * x_norm)))
        
        # Asymmetric cubic interactions with chaotic coupling and dynamic modulation
        asym_cubic = np.sum(x_norm**3 * (1 + 0.4 * np.cos(10 * x_norm)) * 
                           np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                           np.sin(6 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                           (1 + 0.3 * np.sin(14 * np.pi * x_norm[:-1])))
        
        # Perturbed saddle point structure with exponential gradient variations and adaptive scaling
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**4 * 
                       np.cos(0.9 * (x_norm[:-1] + x_norm[1:])) * 
                       np.exp(-0.6 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                       (1 + 0.3 * np.sin(8 * np.pi * x_norm[:-1])) * 
                       (1 + 0.2 * np.cos(12 * np.pi * x_norm[1:])))
        
        # Enhanced polynomial coupling with chaotic repulsive forces and dynamic scaling (modified exponents)
        poly_coupling = np.sum((x_norm[:-1]**3 + x_norm[1:]**3)**6 * 
                              np.exp(-0.7 * (x_norm[:-1] - x_norm[1:])**2) * 
                              (1 + 0.5 * np.cos(15 * np.pi * x_norm[:-1])) * 
                              (1 + 0.3 * np.sin(19 * np.pi * x_norm[1:])))
        
        # Novel chaotic repulsive force field with dynamic modulation and adaptive noise
        repulsion = np.sum(np.exp(-3 * (x_norm**2).sum()) * 
                          np.sin(10 * np.pi * x_norm) * 
                          np.cos(4 * np.pi * x_norm.sum()) * 
                          np.tan(0.7 * x_norm) * 
                          (1 + 0.4 * np.sin(23 * np.pi * x_norm)))
        
        # Additional chaotic noise for robustness testing with dynamic scaling
        noise = 0.2 * np.random.normal(0, 1) * (1 + 0.3 * np.sin(29 * np.pi * x_norm[0] if len(x_norm) > 0 else 0))
        
        # Enhanced chaotic modulation with higher frequency components and increased nonlinearity
        chaos_mod = np.sum(np.sin(25 * np.pi * x_norm) * 
                          np.cos(18 * np.pi * x_norm) * 
                          np.tan(3.2 * x_norm) * 
                          (1 + 0.7 * np.sin(37 * np.pi * x_norm)) * 
                          np.exp(-0.4 * (x_norm**2).sum()) * 
                          np.cos(12 * np.pi * x_norm.sum()))
        
        # Increased polynomial coupling with higher-order terms and dynamic scaling (modified exponents)
        high_order = np.sum((x_norm[:-1]**4 + x_norm[1:]**4)**5 * 
                           np.exp(-0.8 * (x_norm[:-1] - x_norm[1:])**2) * 
                           (1 + 0.6 * np.cos(22 * np.pi * x_norm[:-1])) * 
                           (1 + 0.4 * np.sin(27 * np.pi * x_norm[1:])))
        
        # Enhanced saddle-point structure with additional chaotic perturbations
        enhanced_saddle = np.sum((x_norm[:-1]**3 - x_norm[1:]**3)**4 * 
                               np.sin(1.2 * (x_norm[:-1] + x_norm[1:])) * 
                               np.exp(-0.7 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.4 * np.cos(16 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.sin(20 * np.pi * x_norm[1:])))
        
        # Additional chaotic modulation with fractal-like structure and enhanced nonlinearity
        fractal_mod = np.sum(np.sin(31 * np.pi * x_norm) * 
                            np.cos(24 * np.pi * x_norm) * 
                            np.tan(2.5 * x_norm) * 
                            (1 + 0.8 * np.sin(41 * np.pi * x_norm)) * 
                            np.exp(-0.3 * (x_norm**2).sum()) * 
                            np.cos(15 * np.pi * x_norm.sum()))
        
        # Increased complexity with additional polynomial and trigonometric interactions
        complex_poly = np.sum((x_norm[:-1]**5 + x_norm[1:]**5)**3 * 
                             np.exp(-0.9 * (x_norm[:-1] - x_norm[1:])**2) * 
                             (1 + 0.7 * np.cos(25 * np.pi * x_norm[:-1])) * 
                             (1 + 0.5 * np.sin(30 * np.pi * x_norm[1:])))
        
        # Perturbed gradient structure with enhanced chaotic perturbations
        grad_perturb = np.sum(np.sin(8 * np.pi * x_norm) * 
                             np.cos(12 * np.pi * x_norm) * 
                             (1 + 0.5 * np.sin(16 * np.pi * x_norm)) * 
                             np.exp(-0.4 * np.abs(x_norm)) * 
                             (1 + 0.3 * np.cos(20 * np.pi * x_norm.sum())))
        
        # Additional chaotic modulation with fractal-like structure and enhanced nonlinearity
        final_mod = np.sum(np.sin(35 * np.pi * x_norm) * 
                          np.cos(28 * np.pi * x_norm) * 
                          np.tan(2.8 * x_norm) * 
                          (1 + 0.9 * np.sin(45 * np.pi * x_norm)) * 
                          np.exp(-0.35 * (x_norm**2).sum()) * 
                          np.cos(13 * np.pi * x_norm.sum()))
        
        # Additional polynomial coupling with higher-order terms and dynamic scaling
        additional_poly = np.sum((x_norm[:-1]**6 + x_norm[1:]**6)**2 * 
                                np.exp(-0.95 * (x_norm[:-1] - x_norm[1:])**2) * 
                                (1 + 0.8 * np.cos(28 * np.pi * x_norm[:-1])) * 
                                (1 + 0.6 * np.sin(32 * np.pi * x_norm[1:])))
        
        # Additional chaotic perturbation with enhanced modulation
        extra_chaos = np.sum(np.sin(40 * np.pi * x_norm) * 
                            np.cos(33 * np.pi * x_norm) * 
                            (1 + 0.6 * np.sin(48 * np.pi * x_norm)) * 
                            np.exp(-0.5 * (x_norm**2).sum()) * 
                            np.tan(1.5 * x_norm))
        
        # Introduce more chaotic modulation with higher frequency components
        high_freq_mod = np.sum(np.sin(50 * np.pi * x_norm) * 
                              np.cos(40 * np.pi * x_norm) * 
                              np.tan(3.5 * x_norm) * 
                              (1 + 0.8 * np.sin(55 * np.pi * x_norm)) * 
                              np.exp(-0.3 * (x_norm**2).sum()) * 
                              np.cos(14 * np.pi * x_norm.sum()))
        
        # Add more complex saddle-point interactions with multi-scale perturbations
        multi_saddle = np.sum((x_norm[:-1]**4 - x_norm[1:]**4)**3 * 
                             np.sin(1.5 * (x_norm[:-1] + x_norm[1:])) * 
                             np.exp(-0.8 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                             (1 + 0.5 * np.cos(20 * np.pi * x_norm[:-1])) * 
                             (1 + 0.4 * np.sin(25 * np.pi * x_norm[1:])))
        
        # Introduce fractal-like structure with more complex trigonometric interactions
        fractal_complex = np.sum(np.sin(45 * np.pi * x_norm) * 
                                np.cos(35 * np.pi * x_norm) * 
                                np.tan(2.0 * x_norm) * 
                                (1 + 0.9 * np.sin(50 * np.pi * x_norm)) * 
                                np.exp(-0.4 * (x_norm**2).sum()) * 
                                np.cos(16 * np.pi * x_norm.sum()))
        
        # Add higher-order polynomial coupling with dynamic scaling
        high_order_poly = np.sum((x_norm[:-1]**7 + x_norm[1:]**7)**2 * 
                                np.exp(-0.9 * (x_norm[:-1] - x_norm[1:])**2) * 
                                (1 + 0.9 * np.cos(30 * np.pi * x_norm[:-1])) * 
                                (1 + 0.7 * np.sin(35 * np.pi * x_norm[1:])))
        
        # Introduce chaotic repulsion with multi-scale frequency variations
        multi_repulsion = np.sum(np.exp(-4 * (x_norm**2).sum()) * 
                                np.sin(15 * np.pi * x_norm) * 
                                np.cos(6 * np.pi * x_norm.sum()) * 
                                np.tan(0.8 * x_norm) * 
                                (1 + 0.5 * np.sin(30 * np.pi * x_norm)) * 
                                (1 + 0.4 * np.cos(35 * np.pi * x_norm)))
        
        # Add enhanced chaotic modulation with dynamic amplitude scaling
        enhanced_chaos_mod = np.sum(np.sin(42 * np.pi * x_norm) * 
                                  np.cos(38 * np.pi * x_norm) * 
                                  np.tan(2.7 * x_norm) * 
                                  (1 + 0.95 * np.sin(52 * np.pi * x_norm)) * 
                                  np.exp(-0.38 * (x_norm**2).sum()) * 
                                  np.cos(14 * np.pi * x_norm.sum()))
        
        # Combine all components with increased complexity and more chaotic interactions
        return radial + sin_mod + asym_cubic + saddle + poly_coupling + repulsion + noise + chaos_mod + high_order + enhanced_saddle + fractal_mod + complex_poly + grad_perturb + final_mod + additional_poly + extra_chaos + high_freq_mod + multi_saddle + fractal_complex + high_order_poly + multi_repulsion + enhanced_chaos_mod + 0.1 * np.sum(np.sin(60 * np.pi * x_norm) * np.cos(50 * np.pi * x_norm) * (1 + 0.8 * np.sin(65 * np.pi * x_norm)) * np.exp(-0.2 * (x_norm**2).sum()) * np.cos(18 * np.pi * x_norm.sum()))