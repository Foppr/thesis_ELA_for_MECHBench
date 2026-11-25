import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component with time-varying r parameter
        logistic_sum = 0.0
        r_values = 3.9 + 0.1 * np.sin(np.arange(self.dim) * 0.2)
        x_log = np.abs(x) / 5.0  # Normalize to [0, 1] for logistic map
        for i in range(self.dim):
            logistic_sum += r_values[i] * x_log[i] * (1 - x_log[i])
        
        # Spectral clustering-inspired energy terms with dynamic affinity
        spectral_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                affinity = np.exp(-distance**2 / (2 * (0.5 + 0.3 * np.sin(i * 0.4))))
                spectral_energy += affinity * (x[i]**2 + x[j]**2)
        
        # Fractional Brownian motion component with Hurst parameter modulation
        fbm_term = 0.0
        hurst = 0.3 + 0.4 * np.sin(self.dim * 0.1)
        for i in range(self.dim):
            fbm_term += (x[i]**2) * np.sin(2**i * hurst * np.pi / 4)
        
        # Quantum-like interference pattern with phase modulation
        quantum_interference = 0.0
        for i in range(self.dim):
            phase = np.cos(x[i]) + np.sin(x[i] * 0.5) + 0.1 * np.sin(i * 0.3)
            quantum_interference += np.cos(phase) * np.exp(-x[i]**2 / 10)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.exp(-np.abs(x[i] - x[i+1]) / (0.5 + 0.2 * np.cos(i * 0.2))) * \
                             (x[i]**2 + x[i+1]**2)
        
        # Dynamic conditioning based on variable distribution
        condition_factor = 1.0 + 0.3 * np.sin(np.mean(x)) + \
                          0.2 * np.cos(np.std(x)) * np.log(self.dim + 1) + \
                          0.1 * np.tanh(np.max(np.abs(x)))
        
        # Final combined function value
        return condition_factor * (np.sum(x**2) + 0.1 * np.sum(x**4)) + \
               logistic_sum + spectral_energy + fbm_term + quantum_interference + cross_coupling