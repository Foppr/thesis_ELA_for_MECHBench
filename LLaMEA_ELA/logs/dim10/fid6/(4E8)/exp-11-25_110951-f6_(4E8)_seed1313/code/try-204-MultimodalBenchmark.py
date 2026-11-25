import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-inspired oscillatory components with phase coupling
        quantum_term = 0.0
        for i in range(self.dim):
            quantum_term += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i]) + \
                           np.cos(4 * np.pi * x_norm[i]) * np.sin(5 * np.pi * x_norm[i])
        
        # Spherical regularization with radial basis functions
        sphere_term = np.sum(x_norm**2)
        
        # Saddle-point inducing terms with asymmetric hyperbolic secant modulations
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.5 * np.tanh(2 * x_norm[i]) * (x_norm[i]**2 - 1) + \
                          0.3 * np.sech(3 * x_norm[i]) * (x_norm[i]**3 - x_norm[i])
        
        # Cross-dimensional interaction with fractal-like coupling
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_term += np.sin(2 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(3 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Directional gradient enhancement with exponential decay
        grad_term = 0.0
        for i in range(self.dim):
            grad_term += np.exp(-0.5 * x_norm[i]**2) * np.sin(10 * x_norm[i])
        
        # Combined function with weighted contributions
        return 0.4 * quantum_term + 0.3 * sphere_term + 0.2 * saddle_term + \
               0.05 * fractal_term + 0.05 * grad_term