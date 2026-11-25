import numpy as np

class AsymmetricSaddleGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic conditioning parameters
        self.conditioning_gradients = np.random.uniform(0.5, 3.0, dim)
        self.saddle_weights = np.random.uniform(0.1, 2.0, dim)
        self.noise_amplitudes = np.logspace(-1, 1, dim)
        # Asymmetric saddle point configuration
        self.saddle_positions = np.random.uniform(-3.0, 3.0, dim)
        self.asymmetry_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Asymmetric saddle point contribution
        saddle_term = 0.0
        for i in range(self.dim):
            pos = self.saddle_positions[i]
            asym = self.asymmetry_factors[i]
            # Asymmetric quadratic around saddle points
            diff = x_norm[i] - pos
            saddle_term += self.saddle_weights[i] * (diff ** 2) * np.exp(-0.5 * (diff / asym) ** 2)
            
        # Dynamic conditioning gradient component
        conditioning_term = 0.0
        for i in range(self.dim):
            grad = self.conditioning_gradients[i]
            conditioning_term += grad * (x_norm[i] ** 4) * np.cos(1.5 * x_norm[i])
            
        # Multi-scale interaction terms with asymmetric coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Asymmetric coupling strength
                coupling = (self.saddle_weights[i] + self.saddle_weights[j]) * np.sin(0.3 * (i - j))
                interaction = coupling * np.sin(x_norm[i] * x_norm[j])
                interaction_term += interaction
                
        # Adaptive noise injection
        noise_term = 0.0
        for i in range(min(len(self.noise_amplitudes), self.dim)):
            noise_term += self.noise_amplitudes[i] * np.sin(5.0 * x_norm[i]) * np.random.uniform(-1.0, 1.0)
            
        # Combined function with asymmetric scaling
        result = 0.5 * saddle_term + 0.3 * conditioning_term + 0.2 * interaction_term + 0.1 * noise_term
        
        return result