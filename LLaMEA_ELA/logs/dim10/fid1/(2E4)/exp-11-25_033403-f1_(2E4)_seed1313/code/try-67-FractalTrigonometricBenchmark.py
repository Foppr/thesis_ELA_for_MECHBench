import numpy as np

class FractalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_depth = 3
        self.polynomial_degree = 5
        self.gradient_modulation = 0.8
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar structure with multiple scales
        fractal_term = 0.0
        for scale in range(1, self.fractal_depth + 1):
            scaled_x = x / (2 ** scale)
            fractal_component = np.sum(np.sin(scaled_x) * np.cos(0.5 * scaled_x) * np.exp(-0.1 * scaled_x**2))
            fractal_term += fractal_component / (scale ** 1.5)
        
        # Hybrid polynomial-trigonometric components
        poly_trig_term = 0.0
        for i in range(self.dim):
            # Polynomial terms with trigonometric modulation
            poly_part = x[i]**self.polynomial_degree
            trig_mod = np.sin(2 * np.pi * x[i]) + 0.5 * np.cos(3 * np.pi * x[i])
            poly_trig_term += poly_part * trig_mod
            
        # Adaptive gradient modulation with chaotic perturbations
        grad_mod_term = 0.0
        for i in range(self.dim):
            # Chaotic gradient perturbation using logistic map-like behavior
            chaos_factor = 1.0 + 0.3 * np.sin(5 * x[i]) * np.cos(2 * x[i])
            grad_mod_term += chaos_factor * (x[i]**3 + 0.5 * x[i]**5)
            
        # Multi-scale deceptive valley structure
        valley_term = 0.0
        for i in range(self.dim):
            # Create multiple nested valleys with varying depths and widths
            depth = 1.0 + 0.8 * np.sin(3 * x[i])**2
            width = 1.0 + 0.4 * np.cos(2 * x[i])**2
            valley_term += depth * (x[i] - np.sin(x[i]))**2 / width
            
        # Cross-dimensional harmonic interference with fractal coupling
        cross_harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like harmonic coupling between dimensions
                coupling = np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j]))
                cross_harmonic += coupling / (1 + 0.1 * np.abs(x[i] - x[j]))
                
        # Novel ridge and valley hybrid structure with exponential modulation
        ridge_valley_term = 0.0
        for i in range(self.dim):
            # Combine ridge and valley components with exponential scaling
            ridge_component = np.exp(0.5 * x[i]**2) * np.sin(x[i])**2
            valley_component = np.exp(-0.3 * x[i]**2) * np.cos(x[i])**2
            ridge_valley_term += ridge_component + valley_component
            
        # Additional chaotic noise with fractal characteristics
        noise_term = 0.05 * np.sum(np.sin(10 * x)**3 + 0.3 * np.cos(8 * x)**3)
        
        # Adaptive conditioning with multi-scale exponential components
        condition_term = 0.0
        for i in range(self.dim):
            # Multi-scale conditioning with exponential growth patterns
            scale_factor = (i + 1) * np.exp(0.2 * i)
            condition_term += scale_factor * (x[i]**4 + x[i]**6 + 0.3 * x[i]**8)
            
        return fractal_term + poly_trig_term + grad_mod_term + valley_term + cross_harmonic + ridge_valley_term + noise_term + condition_term