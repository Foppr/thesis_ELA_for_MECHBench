import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        # Precompute constants for noise and conditioning
        self.noise_scale = 0.01
        self.conditioning_factor = 1.0 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying degrees
        poly_result = np.sum(self.conditioning_factor * (x**2 + 0.5 * x**3 + 0.1 * x**4))
        
        # Trigonometric components with varying frequencies
        trig_result = 0.0
        for i in range(self.dim):
            trig_result += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) + 0.5 * np.sin(3.0 * x[i])**2
            
        # Radial basis function component
        rbf_result = 0.0
        for i in range(self.dim):
            rbf_result += np.exp(-0.5 * np.sum((x - x[i])**2)) * np.sin(2.0 * x[i])
            
        # Cross-dimensional coupling with adaptive weights
        coupling_result = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling_result += 0.3 * np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] - 0.3 * x[j])
                
        # Adaptive conditioning and noise
        result = poly_result + trig_result + rbf_result + coupling_result
        
        # Add dynamic noise that depends on position
        noise = np.sum(self.noise_scale * np.sin(10.0 * x) * np.cos(7.0 * x))
        result += noise
        
        return result