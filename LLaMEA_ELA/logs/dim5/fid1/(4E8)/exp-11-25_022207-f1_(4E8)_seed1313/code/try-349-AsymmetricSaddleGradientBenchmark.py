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
        # Fractal-like scaling parameters
        self.fractal_scaling = np.random.uniform(0.1, 1.0, dim)
        self.multi_scale_coupling = np.random.uniform(0.5, 2.0, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Asymmetric saddle point contribution with fractal scaling
        saddle_term = 0.0
        for i in range(self.dim):
            pos = self.saddle_positions[i]
            asym = self.asymmetry_factors[i]
            # Asymmetric quadratic around saddle points with fractal enhancement
            diff = x_norm[i] - pos
            fractal_factor = np.sin(3.0 * diff) * self.fractal_scaling[i]
            saddle_term += self.saddle_weights[i] * (diff ** 2) * np.exp(-0.5 * (diff / asym) ** 2) + fractal_factor
            
        # Dynamic conditioning gradient component with multi-scale coupling
        conditioning_term = 0.0
        for i in range(self.dim):
            grad = self.conditioning_gradients[i]
            # Multi-scale interaction in conditioning
            scale_interaction = 0.0
            for j in range(self.dim):
                if i != j:
                    scale_interaction += self.multi_scale_coupling[i, j] * np.sin(0.5 * (x_norm[i] - x_norm[j]))
            conditioning_term += grad * (x_norm[i] ** 4) * np.cos(1.5 * x_norm[i]) + scale_interaction
            
        # Multi-scale interaction terms with asymmetric coupling and fractal structure
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Asymmetric coupling strength with fractal influence
                coupling = (self.saddle_weights[i] + self.saddle_weights[j]) * np.sin(0.3 * (i - j))
                # Fractal interaction term
                fractal_interaction = np.sin(2.0 * (x_norm[i] + x_norm[j])) * self.fractal_scaling[i] * self.fractal_scaling[j]
                interaction = coupling * np.sin(x_norm[i] * x_norm[j]) + fractal_interaction
                interaction_term += interaction
                
        # Adaptive noise injection with fractal pattern
        noise_term = 0.0
        for i in range(min(len(self.noise_amplitudes), self.dim)):
            # Fractal noise pattern
            fractal_noise = np.sin(7.0 * x_norm[i]) * self.fractal_scaling[i]
            noise_term += self.noise_amplitudes[i] * (np.sin(5.0 * x_norm[i]) + fractal_noise) * np.random.uniform(-1.0, 1.0)
            
        # Combined function with asymmetric scaling and enhanced complexity
        result = 0.4 * saddle_term + 0.3 * conditioning_term + 0.2 * interaction_term + 0.1 * noise_term
        
        return result