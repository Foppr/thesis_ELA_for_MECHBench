import numpy as np

class AsymmetricHillClimbingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Asymmetric hill-climbing components with varying steepness and orientation
        hill_asym = np.sum(np.abs(x_norm)**(3 + 0.5 * np.sin(10 * x_norm)) * 
                           np.exp(-0.5 * np.sum((x_norm - 0.3)**2)) + 
                           np.abs(x_norm)**(2.5 + 0.3 * np.cos(15 * x_norm)) * 
                           np.exp(-0.3 * np.sum((x_norm + 0.4)**2)))
        
        # Cross-dimensional coupling with directional bias and varying interaction strength
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x_norm[i] * x_norm[j] * 
                                  np.exp(-0.1 * (x_norm[i] - x_norm[j])**2) * 
                                  np.sin(5 * (x_norm[i] + x_norm[j])))
        
        # Dynamic scaling factor that varies with position to create non-uniform terrain
        scale_factor = 1.0 + 0.5 * np.sin(2 * np.sum(x_norm**2)) + 0.3 * np.cos(3 * np.sum(x_norm))
        
        # Multi-peak landscape with irregular spacing and variable heights
        peaks = 0
        for i in range(20):
            center = np.full(self.dim, (i % 5) * 0.5 - 1.0)
            height = 1.0 + 0.5 * np.sin(i * 0.5)
            peaks += height * np.exp(-2 * np.sum((x_norm - center)**2))
        
        # Rugged terrain with directional bias and controlled roughness
        rugged = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * 
                        np.exp(-0.5 * np.abs(x_norm)) + 
                        np.cos(25 * x_norm) * np.sin(18 * x_norm) * 
                        np.exp(-0.3 * np.abs(x_norm)))
        
        # Nonlinear transformation with asymmetric behavior around different axes
        nonlinear = np.sum(np.tanh(5 * x_norm)**2 + 0.3 * np.sinh(3 * x_norm)**2)
        
        # Combine all components with varying weights
        result = 0.25 * hill_asym + 0.2 * cross_coupling + 0.15 * scale_factor + 0.2 * peaks + 0.12 * rugged + 0.08 * nonlinear
        
        # Add controlled noise term
        noise_factor = 0.02 * (1 + np.abs(np.sum(x_norm**4)))
        dynamic_noise = noise_factor * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise