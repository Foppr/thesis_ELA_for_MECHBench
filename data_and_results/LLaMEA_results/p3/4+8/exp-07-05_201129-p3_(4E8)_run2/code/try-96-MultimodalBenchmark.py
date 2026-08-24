import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Enhanced fractal component using modified logistic map with multiple parameters
        r = np.sqrt(np.sum(x_norm**2))
        logistic_map = 4.0 * r * (1 - r)
        fractal_term = r**2.5 * np.exp(-r**2) * logistic_map
        
        # Multi-peak sinusoidal interaction with adaptive amplitudes and frequencies
        peak_term = 0.0
        for i in range(min(6, self.dim)):
            freq = (i + 1) * 3.5  # Slight increase in frequency
            amp = 1.0 / (1.0 + i * 0.3)
            peak_term += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial polynomial with enhanced exponential modulation and multiple local minima
        radial_poly = np.sum((x_norm**2 + 0.05) * np.exp(-0.3 * x_norm**2))
        
        # Angular coupling with higher-order harmonic interactions
        angular_coupling = 0.0
        if self.dim > 1:
            for i in range(min(5, self.dim)):
                for j in range(i+1, min(5, self.dim)):
                    angular_coupling += np.sin((i+1) * (j+1) * np.arctan2(x_norm[j], x_norm[i])) * np.cos((i+1) * (j+1) * np.arctan2(x_norm[i], x_norm[j]))
        
        # Cross-term with sigmoid modulation for smoother gradients
        cross_term = np.sum(1.0 / (1.0 + np.exp(-2.0 * x_norm)) * np.sin(4.0 * x_norm)**2)
        
        # Additional chaotic component with delayed feedback and multiple time scales
        delayed_feedback = np.sin(r * 8.0) * np.cos(r * 4.0) if r > 0.05 else 0.0
        chaotic_term = (3.5 * r * (1 - r**2)) * delayed_feedback * np.exp(-0.1 * r**2)
        
        # Introduce a new term: hyperchaotic interaction with higher dimensional coupling
        hyperchaos_term = 0.0
        if self.dim >= 4:
            for i in range(4):
                for j in range(i+1, min(6, self.dim)):
                    for k in range(j+1, min(6, self.dim)):
                        hyperchaos_term += np.sin(x_norm[i] * x_norm[j] * x_norm[k]) * np.cos(x_norm[i] + x_norm[j] + x_norm[k])
        
        # Add cubic polynomial coupling between dimensions to increase complexity
        cubic_coupling = 0.0
        if self.dim >= 3:
            for i in range(min(3, self.dim)):
                for j in range(i+1, min(4, self.dim)):
                    cubic_coupling += (x_norm[i]**3) * (x_norm[j]**3)
        
        # Combine all terms with dynamic weights based on dimensionality
        dim_factor = 1.0 + 0.08 * (self.dim - 1)
        result = (0.25 * fractal_term + 
                 0.20 * peak_term + 
                 0.18 * radial_poly + 
                 0.15 * angular_coupling + 
                 0.08 * cross_term + 
                 0.07 * chaotic_term + 
                 0.06 * hyperchaos_term +  # Reduced weight
                 0.05 * cubic_coupling) * dim_factor
        
        return result