import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with logistic map modulation
        chaotic_grad = 0.0
        r = 3.9
        for i in range(self.dim):
            xi = x[i]
            chaotic_grad += xi**2 * np.sin(r * xi) * np.cos(r * xi**2)
        
        # Sinusoidal perturbation with multi-frequency harmonic interaction
        sin_pert = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0]
        for i in range(self.dim):
            for f in frequencies:
                sin_pert += np.sin(f * x[i]) * np.cos(f * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Saddle-point attractor landscape with hyperbolic tangent coupling
        saddle = 0.0
        for i in range(self.dim):
            saddle += (np.tanh(x[i])**3) * (x[i]**2) + (np.tanh(x[i] / 2.0)**2) * np.cos(x[i])
        
        # Multi-resolution harmonic interference with varying amplitudes and phases
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x[i] - x[j])
                amplitude = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
                phase = j * np.pi / (self.dim + 1)
                interference += amplitude * np.sin(dist + phase) * np.cos(dist * 2.0 + phase)
        
        # Dynamic conditioning with exponential scaling and adaptive weight
        condition = 1.0
        for i in range(self.dim):
            condition *= (1.0 + 0.2 * np.exp(-0.5 * x[i]**2) * np.sin(x[i]))
        
        # Combine all components with normalization
        result = condition * (chaotic_grad + sin_pert + saddle + interference)
        
        # Add small random noise to break symmetry and increase robustness
        noise = 0.001 * np.random.rand()
        
        return result + noise