import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with enhanced complexity
        self.r = 3.8  # Slightly different logistic map parameter for more complexity
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using logistic map with modified iterations
        seq = np.zeros(self.dim)
        x = 0.5  # Initial value
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic polynomial component with higher-order terms
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            result += chaotic_factor * (x[i]**5 - 5*x[i]**4 + 10*x[i]**3 - 10*x[i]**2 + 5*x[i] - 1)
            
        # Enhanced trigonometric coupling with multiple phase interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j] + np.sin(x[i] + x[j])
                result += 0.7 * np.sin(3 * np.pi * x[i] + phase) * np.cos(3 * np.pi * x[j] + phase)
                
        # Adaptive spherical penalty with chaotic scaling
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        penalty_weight = 0.5 + 0.2 * np.mean(self.chaotic_sequence)
        result += penalty_weight * np.sum((x - center)**2)
        
        # Multi-frequency chaotic oscillation
        for i in range(self.dim):
            result += 0.3 * np.sin(15 * x[i] * self.chaotic_sequence[i]) + 0.2 * np.cos(25 * x[i] * self.chaotic_sequence[i])
            
        # Add a global minimum attractor with chaotic modulation
        global_attraction = 0.15 + 0.05 * np.mean(self.chaotic_sequence)
        result += global_attraction * np.sum(x**2)
        
        # Additional chaotic noise component to increase landscape complexity
        noise_factor = np.mean(np.sin(self.chaotic_sequence * 10))
        result += 0.1 * noise_factor * np.sum(np.abs(x))
        
        return result