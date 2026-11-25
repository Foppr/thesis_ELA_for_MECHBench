import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired oscillatory component with dynamic frequency and phase
        quantum_term = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.4 * i)
            phase = 0.3 * np.cos(0.5 * i)
            quantum_term += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function with adaptive centers and time-varying variances
        rbf_term = 0.0
        num_centers = min(7, self.dim)
        for i in range(num_centers):
            center = -4.0 + 8.0 * np.random.rand()
            variance = 0.2 + 0.6 * np.sin(0.3 * i) ** 2
            rbf_term += np.exp(-0.5 * ((x[i] - center) ** 2) / variance)
        
        # Entropy-based ruggedness with adaptive exponentiation and multi-scale interactions
        entropy_term = 0.0
        for i in range(self.dim-1):
            diff = x[i] - x[i+1]
            entropy_term += np.abs(diff) * np.exp(-np.abs(diff)) * (1 + 0.4 * np.sin(3.0 * x[i]))
        
        # Novel fractal coupling mechanism based on information-theoretic distance
        fractal_coupling = 0.0
        for i in range(self.dim-2):
            dist = np.abs(x[i] - x[i+1]) + 1e-8
            fractal_coupling += (x[i] * x[i+2]) / dist * np.cos(0.5 * x[i]) * np.exp(-0.05 * (x[i] ** 2))
        
        # Sine-wave modulation with dynamic amplitude and phase, enhanced with polynomial scaling
        modulated_term = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.6 * np.sin(0.7 * i)
            phase = 0.25 * np.cos(0.4 * i)
            modulated_term += amp * np.sin(x[i] + phase) * np.exp(-0.03 * x[i]**2) * (1 + 0.1 * x[i]**2)
        
        # Fractal-inspired scaling based on solution entropy and dimensionality
        if self.dim > 1:
            entropy = np.std(x) / (np.max(x) - np.min(x) + 1e-8) if np.max(x) != np.min(x) else 0.0
            scale_factor = 1.0 + 0.6 * entropy + 0.2 * np.log(self.dim)
        else:
            scale_factor = 1.0
        
        # Add dynamic noise based on dimensionality and solution proximity to boundaries
        noise = 0.0
        for i in range(self.dim):
            boundary_distance = min(np.abs(x[i] - (-5.0)), np.abs(x[i] - 5.0))
            noise += 0.01 * boundary_distance * np.sin(2.0 * x[i]) * np.cos(0.5 * x[i])
        
        # Combine all terms with enhanced nonlinearity and coupling
        result = (quantum_term + rbf_term + entropy_term + fractal_coupling + modulated_term) * scale_factor + noise
        
        # Add a global scaling factor to increase overall complexity
        return result * (1.0 + 0.3 * np.sin(0.1 * self.dim))