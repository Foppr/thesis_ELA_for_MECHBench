import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal chaotic component with dynamic frequency modulation
        chaotic_component = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i])
            chaotic_component += np.sin(freq * x[i]) * np.cos(0.4 * x[i]**2) * np.tanh(x[i])
        
        # Radial basis function with dynamic width and orientation
        rbf_component = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 1.0 + 0.5 * np.sin(0.2 * (x[i] + x[j]))
                orientation = np.cos(0.3 * x[i]) * np.sin(0.3 * x[j])
                rbf_component += orientation * np.exp(-0.5 * (dist / width)**2)
        
        # Polynomial coupling with hyperbolic tangent and exponential decay
        poly_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.tanh(x[i] * x[j]) + 0.3 * np.sin(x[i] + x[j])
                term = (x[i]**2 + x[j]**2) * coupling * np.exp(-0.1 * (x[i] - x[j])**2)
                poly_component += term
        
        # Asymmetric skewing with fractal-like scaling
        skew_component = 0
        for i in range(self.dim):
            skew_factor = 1.0 + 0.4 * np.sin(0.5 * x[i]) + 0.2 * np.cos(0.7 * x[i]**2)
            skew_component += np.tanh(x[i]) * skew_factor
        
        # Dynamic conditioning with polynomial and exponential terms
        cond_component = 0
        for i in range(self.dim):
            cond_component += (x[i]**3 + 0.5 * x[i]**2) * np.tanh(x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Anti-symmetric noise component with multi-scale structure
        noise_component = 0
        for i in range(self.dim):
            noise_component += 0.1 * (np.sin(3 * x[i]) * np.cos(5 * x[i]) - 
                                   np.cos(3 * x[i]) * np.sin(5 * x[i])) * np.tanh(x[i])
        
        # Fractal-like recursive coupling with dynamic weights
        fractal_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.3 * np.sin(0.2 * (x[i] + x[j]))
                fractal_component += weight * (x[i] - x[j]) * np.tanh(x[i] + x[j]) * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Global scaling factor based on dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.15) + 0.1 * np.cos(self.dim * 0.1)
        
        # Combine all components with optimized weights
        return scale_factor * (0.3 * chaotic_component + 0.25 * rbf_component + 
                              0.2 * poly_component + 0.1 * skew_component + 
                              0.08 * cond_component + 0.05 * fractal_component) + noise_component