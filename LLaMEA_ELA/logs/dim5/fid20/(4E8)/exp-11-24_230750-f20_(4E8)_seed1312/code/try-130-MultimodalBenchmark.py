import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for recurrent dynamics
        self.chaos_params = np.random.rand(dim) * 2.0 - 1.0
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic recurrent neural network dynamics with varying activation thresholds
        chaotic_sum = 0.0
        for i in range(self.dim):
            # Dynamic threshold based on position and chaos parameter
            threshold = 0.5 + 0.5 * np.sin(x[i] * np.pi / 5.0) + self.chaos_params[i]
            
            # Recurrent interaction with previous dimensions
            recurrent = 0.0
            for j in range(i):
                weight = 0.3 * np.cos((i - j) * np.pi / (self.dim + 1))
                recurrent += weight * np.tanh(x[j] - threshold)
            
            # Chaotic activation with dynamic scaling
            activation = np.sin(x[i]**2 + recurrent) * np.exp(-np.abs(x[i]) / 5.0)
            chaotic_sum += activation
            
        # Multi-scale harmonic interference with adaptive frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            phase = 0.2 * np.cos(x[i] * freq)
            amplitude = 1.0 + 0.3 * np.sin(x[i] * 0.5)
            harmonic += amplitude * np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2)
        
        # Rugged landscape with multiple overlapping polynomial basins
        basin = 0.0
        for i in range(min(6, self.dim)):
            center = -3.0 + 6.0 * (i / max(1, self.dim - 1))
            width = 1.0 + 0.2 * np.sin(i * np.pi / 4.0)
            power = 2.0 + 0.5 * np.cos(i * np.pi / 3.0)
            basin += (x[i] - center)**power / (width**power + 1e-8)
        
        # Dynamic conditioning with position-dependent scaling
        condition = 1.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(x[i] * np.pi / 2.5)
            condition *= scale_factor
        
        # Combine all components with nonlinear coupling
        result = condition * (chaotic_sum + harmonic + basin)
        
        # Add small random noise to break symmetry and increase robustness
        noise = 0.005 * np.random.rand()
        
        return result + noise