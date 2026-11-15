import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Enhanced fractal component with modified tent map and additional chaos
        r = np.sqrt(np.sum(x_norm**2))
        tent_map = np.where(r < 0.25, 4.0 * r, np.where(r < 0.5, 1.0 - 2.0 * (r - 0.25), 4.0 * (r - 0.5)))
        fractal_term = r**2.5 * np.exp(-r**2) * tent_map
        
        # Multi-peak sinusoidal interaction with frequency modulation and dynamic amplitudes
        peak_term = 0.0
        for i in range(min(6, self.dim)):
            freq = (i + 1) * 1.5 + 0.5 * np.sin(i * 0.7)
            amp = 1.0 / (1.0 + 0.3 * i + 0.2 * np.cos(i * 0.5))
            peak_term += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial polynomial with multiple local minima and exponential modulation
        radial_poly = np.sum((x_norm**2 + 0.05) * np.exp(-0.3 * x_norm**2))
        
        # Angular coupling with harmonic interactions and phase shifts
        angular_coupling = 0.0
        if self.dim > 1:
            for i in range(min(3, self.dim)):
                for j in range(i+1, min(3, self.dim)):
                    angle = np.arctan2(x_norm[j], x_norm[i])
                    angular_coupling += np.sin((i+1) * (j+1) * angle + i * 0.3) * np.cos((i+1) * (j+1) * angle + j * 0.4)
        
        # Cross-term with enhanced gradient and nonlinearity
        cross_term = np.sum(np.tanh(3.0 * x_norm) * np.sin(3.0 * x_norm)**3)
        
        # Additional chaotic logistic map with multi-scale feedback
        logistic = 3.9 * r * (1 - r)
        delayed_feedback = np.sin(r * 15.0) if r > 0.05 else 0.0
        logistic_term = logistic * delayed_feedback * np.exp(-0.1 * r**2)
        
        # Additional harmonic potential with multiple local minima
        harmonic_potential = 0.0
        for i in range(min(4, self.dim)):
            harmonic_potential += np.sin(2.0 * x_norm[i])**4 + 0.5 * np.cos(3.0 * x_norm[i])**2
        
        # Combine all terms with optimized weights and dimensionality scaling
        dim_factor = 1.0 + 0.15 * (self.dim - 1)
        result = (0.25 * fractal_term + 
                 0.3 * peak_term + 
                 0.15 * radial_poly + 
                 0.1 * angular_coupling + 
                 0.08 * cross_term + 
                 0.07 * logistic_term + 
                 0.05 * harmonic_potential) * dim_factor
        
        return result