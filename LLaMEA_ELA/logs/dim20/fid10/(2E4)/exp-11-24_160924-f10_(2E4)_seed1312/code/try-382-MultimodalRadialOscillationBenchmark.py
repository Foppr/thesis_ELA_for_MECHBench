import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic sinusoidal components
        self.sin_freq = np.random.uniform(5.0, 15.0, dim)
        self.sin_amp = np.random.uniform(2.0, 6.0, dim)
        self.sin_phase = np.random.uniform(0.0, 4*np.pi, dim)
        # Initialize quantum-like radial basis functions
        self.rbf_centers = np.random.uniform(-4.8, 4.8, (dim, dim))
        self.rbf_widths = np.random.uniform(0.1, 2.5, dim)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, dim)
        # Initialize tensor-based polynomial interactions
        self.poly_coeffs = np.random.uniform(-1.2, 1.2, (dim, dim, dim))
        # Additional chaotic parameters
        self.chaos_factor = np.random.uniform(0.8, 3.0, dim)
        self.quantum_phase = np.random.uniform(0.0, np.pi, dim)
        self.tensor_rank = np.random.randint(3, 6, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic sinusoidal components with quantum phase modulation
        for i in range(self.dim):
            # Base chaotic sinusoidal term
            result += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            # Quantum-like oscillation component
            result += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.quantum_phase[i]) * np.cos(self.chaos_factor[i] * x[i])
            
        # Quantum-like radial basis functions with complex interaction
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.rbf_centers[i][j])**2
                rbf_sum += np.exp(-distance / (2 * self.rbf_widths[i]**2)) * np.sin(x[j])
            result += self.rbf_weights[i] * rbf_sum
            
        # Tensor-based polynomial interactions with higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    interaction = self.poly_coeffs[i][j][k] * x[i] * x[j] * x[k]
                    result += interaction
                    
        # Add chaotic polynomial terms with tensor rank modulation
        for i in range(self.dim):
            power = self.tensor_rank[i]
            result += 0.2 * x[i]**power - 0.8 * x[i]**(power-1) + 0.4 * x[i]**(power-2) + 0.1 * x[i]
            
        # Add tensor-based cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.03 * x[i]**2 * x[j] * x[k] + 0.02 * x[i] * x[j]**2 * x[k] + 0.01 * x[i] * x[j] * x[k]**2
                    
        # Add global chaotic scaling factor
        chaos_term = np.prod(np.sin(x) + 1.0)
        result *= (1.0 + 0.3 * chaos_term)
        
        return result