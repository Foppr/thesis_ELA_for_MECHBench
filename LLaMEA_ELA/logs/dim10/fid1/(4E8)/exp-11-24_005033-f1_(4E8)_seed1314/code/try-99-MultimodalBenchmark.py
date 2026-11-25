import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base multimodal component with fractal-like recursive interactions
        result = np.sum(np.log(1.0 + x**2 / 25.0)) + 3.0 * np.sum(np.cos(15 * x) * np.sin(20 * x)) + 0.02 * np.sum(x**4)
        
        # Dynamic elliptic conditioning with fractal scaling
        ellipsoid_term = 0.0
        for i in range(self.dim):
            ellipsoid_term += (10**(2*i/(self.dim-1)) * x[i]**2)
        result += 0.1 * ellipsoid_term
        
        # Introduce recursive fractal coupling terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like interaction with recursive scaling
                scale = 1.0 / (1.0 + np.abs(x[i] - x[j]))
                result += 0.05 * np.sin(20 * x[i]) * np.cos(20 * x[j]) * scale * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Add recursive chaotic component with self-similar structure and modified frequencies
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(30 * x[i]) * np.cos(35 * x[i]) * np.sin(40 * x[i]) * np.exp(-0.02 * x[i]**2)
        result += 0.08 * chaos_term
        
        # Enhanced cross-dimensional couplings with non-separable interactions and dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_scale = 1.0 + 0.5 * np.sin(0.5 * (x[i] + x[j]))
                result += 0.02 * np.sin(15 * (x[i] + x[j])) * np.cos(15 * (x[i] - x[j])) * dynamic_scale * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add higher-order polynomial coupling with adaptive exponents and fractal-like modulation
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i]**3 + x[j]**3) * np.sin(10 * (x[i] + x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        result += 0.03 * poly_coupling
        
        # Adaptive gradient modulation with recursive penalty and dynamic frequency adjustment
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.abs(np.cos(15 * x[i]) * np.sin(20 * x[i])) * (1.0 + 0.3 * np.sin(0.7 * x[i]))
        result += 0.15 * (grad_mod**2) * np.exp(-0.01 * np.sum(x**2))
        
        # Add a novel basin attraction component with multiple local minima and recursive structure
        basin_term = 0.0
        for k in range(7):
            phase = k * np.pi / 7
            basin_term += np.sum(np.sin(10 * (x + phase)) * np.cos(12 * (x + phase)) * np.exp(-0.03 * (x + phase)**2))
        result += 0.04 * basin_term
        
        # Add a novel multi-scale harmonic component with recursive frequency modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sum(np.sin(50 * x[i] + np.sin(25 * x[i])) * np.cos(45 * x[i] + np.cos(20 * x[i])))
        result += 0.06 * harmonic_term
        
        # Add a dynamic conditioning term with fractal-like scaling
        dynamic_conditioning = 0.0
        for i in range(self.dim):
            dynamic_conditioning += (10**(3*i/(self.dim-1)) * np.sin(x[i])**2)
        result += 0.12 * dynamic_conditioning
        
        return result