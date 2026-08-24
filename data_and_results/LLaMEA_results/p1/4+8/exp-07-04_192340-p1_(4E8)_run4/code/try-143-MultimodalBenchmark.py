import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
        # Add a chaotic parameter that influences the landscape
        self.chaotic_param = np.random.uniform(0.5, 2.0)
        # Add a new hyperparameter for controlling the penalty strength
        self.penalty_strength = np.random.uniform(0.001, 0.01)
        # Add a new sinusoidal frequency modifier
        self.freq_modifier = np.random.uniform(0.5, 1.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.5
            # Sinusoidal components with varying frequencies and amplitudes
            freq = (i + 1) * self.freq_modifier[i]
            result += 5 * np.sin(x_rot[i] * freq * np.pi / 2) * np.cos(x_rot[i] * freq * np.pi / 4)
            # Logarithmic barrier to prevent divergence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 2)
            result += log_term * (i + 1) * 0.15
            # Additional chaotic component using a tent map-like term
            chaotic = np.sin(np.pi * x_rot[i] * np.sin(x_rot[i] * self.chaotic_param))
            result += chaotic * (i + 1) * 0.1
            # Exponential decay term to create ruggedness
            exp_term = np.exp(-0.1 * np.abs(x_rot[i]))
            result += exp_term * (i + 1) * 0.05
            # Add a composite sinusoidal term for increased multimodality
            composite = np.sin(x_rot[i] * np.pi * (i + 1)) * np.cos(x_rot[i] * np.pi * (i + 1) / 2)
            result += composite * (i + 1) * 0.08
            # Add a new hyperbolic tangent component for additional ruggedness
            tanh_component = np.tanh(x_rot[i] * (i + 1)) * np.sin(x_rot[i] * (i + 1) * 0.5)
            result += tanh_component * (i + 1) * 0.03
            # Add a new periodic component with varying amplitude
            periodic = np.sin(x_rot[i] * (i + 1) * 2 * np.pi) * np.cos(x_rot[i] * (i + 1) * 2 * np.pi)
            result += periodic * (i + 1) * 0.02
        
        # Add a hybrid penalty mechanism combining multiple penalty types
        penalty = 0.0
        for i in range(self.dim):
            # Quadratic penalty for large values
            penalty += self.penalty_strength * (x_rot[i] ** 2)
            # Logarithmic penalty for extreme values
            penalty += 0.001 * np.log(1 + np.abs(x_rot[i]))
            # Exponential penalty for very large values
            penalty += 0.0005 * np.exp(np.abs(x_rot[i]) - 4)
        result += penalty
        
        return result