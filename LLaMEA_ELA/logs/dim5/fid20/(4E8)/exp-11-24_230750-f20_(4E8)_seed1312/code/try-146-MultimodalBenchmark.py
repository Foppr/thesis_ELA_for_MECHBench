import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient component with logistic map modulation and sine coupling
        chaotic_grad = 0.0
        r = 4.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_grad += xi**3 * np.sin(r * xi) * np.cos(r * xi**2) + 0.5 * np.sin(xi**3) * np.cos(xi)
        
        # Multi-frequency sinusoidal perturbation with exponential decay and phase shifts
        sin_pert = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0, 5.0]
        phases = [0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
        for i in range(self.dim):
            for f, p in zip(frequencies, phases):
                sin_pert += np.sin(f * x[i] + p) * np.exp(-0.1 * x[i]**2) * (1.0 + 0.3 * np.sin(f * x[i]))
        
        # Saddle-point attractor landscape with hyperbolic tangent coupling and polynomial correction
        saddle = 0.0
        for i in range(self.dim):
            saddle += (np.tanh(x[i])**4) * (x[i]**2) + (np.tanh(x[i] / 3.0)**3) * np.cos(x[i]) + 0.1 * x[i]**4
        
        # Multi-resolution harmonic interference with dynamic amplitudes and adaptive phases
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                dist = np.abs(x[i] - x[j])
                amplitude = 1.5 + 0.8 * np.sin(i * np.pi / self.dim) * np.cos(j * np.pi / self.dim)
                phase = j * np.pi / (self.dim + 2) + 0.5 * np.sin(i)
                interference += amplitude * np.sin(dist + phase) * np.cos(dist * 3.0 + phase) * np.exp(-0.05 * dist**2)
        
        # Dynamic conditioning with exponential scaling, adaptive weights, and polynomial modulation
        condition = 1.0
        for i in range(self.dim):
            condition *= (1.0 + 0.3 * np.exp(-0.4 * x[i]**2) * np.sin(x[i]) + 0.2 * x[i]**3)
        
        # Add polynomial cross-terms for increased complexity and interaction
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x[i]**2) * (x[j]**3) * np.sin(x[i] + x[j])
        
        # Combine all components with normalization and adaptive scaling
        result = condition * (chaotic_grad + sin_pert + saddle + interference + cross_terms)
        
        # Add small random noise to break symmetry and increase robustness
        noise = 0.001 * np.random.rand()
        
        return result + noise