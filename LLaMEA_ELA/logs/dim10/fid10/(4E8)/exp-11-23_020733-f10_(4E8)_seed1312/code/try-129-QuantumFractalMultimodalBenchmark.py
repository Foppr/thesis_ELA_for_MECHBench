import numpy as np

class QuantumFractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.uniform(0.5, 2.0, dim)
        self.alpha = np.random.uniform(0.1, 0.5, dim)
        # Fractal Brownian motion parameters
        self.hurst = np.random.uniform(0.3, 0.8, dim)
        # Neural network gating parameters
        self.weights = np.random.normal(0, 0.5, (dim, dim))
        self.biases = np.random.normal(0, 0.3, dim)
        # Adaptive scaling factors
        self.scale_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Quantum harmonic potential terms
        for i in range(self.dim):
            quantum_term = 0.5 * self.omega[i] * (x[i]**2) + 0.25 * self.alpha[i] * (x[i]**4)
            result += quantum_term
            
        # Fractal Brownian motion based landscape modulation
        for i in range(self.dim):
            # Fractional Brownian motion with Hurst parameter
            fbm_component = np.sin(self.hurst[i] * x[i]) * np.cos(self.hurst[i] * x[i]**2)
            result += 0.3 * fbm_component
            
        # Neural network gating mechanism
        for i in range(self.dim):
            # Gating function with adaptive weights and biases
            gating_input = np.dot(self.weights[i], x) + self.biases[i]
            gating_output = 1.0 / (1.0 + np.exp(-gating_input))
            result += 0.4 * gating_output * x[i]**2
            
        # Multi-scale fractal structure with adaptive scaling
        for i in range(self.dim):
            scale = self.scale_factors[i]
            fractal_term = np.sin(scale * x[i]) * np.cos(scale * x[i]**3) * np.exp(-0.1 * np.abs(x[i]))
            result += 0.2 * fractal_term
            
        # Cross-dimensional quantum coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.sin(self.omega[i] * x[i]) * np.cos(self.omega[j] * x[j])
                result += 0.15 * coupling * (x[i]**2 + x[j]**2)
                
        # Adaptive conditioning with fractal modulation
        fractal_condition = 1.0 + 0.3 * np.sin(np.sum(x**3) / self.dim)
        result *= fractal_condition
        
        # Add quantum noise with fractal characteristics
        quantum_noise = np.sum(np.sin(self.hurst * x) * np.random.normal(0, 0.1, self.dim))
        result += 0.05 * quantum_noise
        
        return result