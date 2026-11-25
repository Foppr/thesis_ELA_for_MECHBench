import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired oscillatory component with dynamic frequency
        quantum_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(0.3 * i)
            quantum_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function with adaptive centers and time-varying variances
        rbf_term = 0.0
        num_centers = min(5, self.dim)
        for i in range(num_centers):
            center = -4.5 + 9.0 * np.random.rand()
            variance = 0.3 + 0.7 * np.sin(0.2 * i) ** 2
            rbf_term += np.exp(-0.5 * ((x[i] - center) ** 2) / variance)
        
        # Entropy-based ruggedness with adaptive exponentiation
        entropy_term = 0.0
        for i in range(self.dim-1):
            diff = x[i] - x[i+1]
            entropy_term += np.abs(diff) * np.exp(-np.abs(diff)) * (1 + 0.3 * np.sin(5.0 * x[i]))
        
        # Novel coupling mechanism based on information-theoretic distance
        info_coupling = 0.0
        for i in range(self.dim-2):
            dist = np.abs(x[i] - x[i+1]) + 1e-8
            info_coupling += (x[i] * x[i+2]) / dist * np.cos(0.4 * x[i])
        
        # Sine-wave modulation with dynamic amplitude and phase
        modulated_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.6 * i)
            phase = 0.2 * np.cos(0.3 * i)
            modulated_term += amp * np.sin(x[i] + phase) * np.exp(-0.05 * x[i]**2)
        
        # Dynamic scaling based on solution entropy
        entropy = np.std(x) / (np.max(x) - np.min(x) + 1e-8) if np.max(x) != np.min(x) else 0.0
        scale_factor = 1.0 + 0.5 * entropy
        
        return (quantum_term + rbf_term + entropy_term + info_coupling + modulated_term) * scale_factor