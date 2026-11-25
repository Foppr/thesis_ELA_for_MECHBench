import numpy as np

class ExponentialTentHyperbolicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute tent map parameters for chaotic behavior
        self.tent_mu = 1.8 + 0.4 * np.random.rand(dim)
        # Precompute exponential radial basis centers and scales
        self.centers = np.random.uniform(-1, 1, dim)
        self.scales = 0.5 + 1.5 * np.random.rand(dim)
        # Precompute hyperbolic coupling weights with increased variability
        self.hyperbolic_weights = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Precompute chaotic sequence for dynamic conditioning
        self.chaotic_seq = np.array([self._tent_map(0.5, self.tent_mu[i]) for i in range(dim)])
        
    def _tent_map(self, x, mu):
        if x < 0.5:
            return mu * x
        else:
            return mu * (1 - x)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential radial basis component with dynamic scales
        exp_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            exp_sum += np.exp(-self.scales[i] * dist) * np.sin(4 * np.sqrt(dist))
        
        # Chaotic tent map component with dynamic scaling
        chaotic_sum = 0.0
        for i in range(self.dim):
            x_chaos = self.chaotic_seq[i]
            chaotic_sum += np.tanh(x_chaos) * np.sin(2 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Hyperbolic coupling component with cross-dimensional interactions
        hyperbolic_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.hyperbolic_weights[i, j] * np.tanh(x_norm[i] - x_norm[j])
                    hyperbolic_sum += coupling * np.exp(-0.2 * coupling**2)
        
        # Multi-modal harmonic component with varying phases
        harm_sum = 0.0
        for i in range(self.dim):
            phase = np.pi * np.cos(i * np.pi / self.dim)
            harm_sum += np.tanh(2 * x_norm[i] + phase) * np.sin(4 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Enhanced tunneling pathway component with stronger polynomial barriers
        tunnel_sum = 0.0
        for i in range(self.dim):
            barrier = 1.0 + 0.5 * np.tanh(x_norm[i] * 4)  # Increased barrier strength
            tunnel_sum += barrier * (x_norm[i]**7 - x_norm[i]**3) * np.exp(-0.15 * x_norm[i]**2)  # Higher order polynomial
        
        # Combined landscape with adaptive scaling
        result = 0.3 * exp_sum + 0.18 * chaotic_sum + 0.28 * hyperbolic_sum + 0.17 * harm_sum + 0.07 * tunnel_sum
        
        # Dynamic conditioning factor based on chaotic sequence and input magnitude
        condition_factor = 1.0
        for i in range(self.dim):
            chaos_factor = np.tanh(self.chaotic_seq[i]) * (1.0 + 0.3 * np.cos(x_norm[i]))
            condition_factor *= (1.0 + 0.5 * np.abs(x_norm[i]) + 0.2 * x_norm[i]**4 + 0.1 * chaos_factor)
        
        # Final transformation with global scaling and noise modulation
        noise = 0.035 * np.sum(np.sin(x_norm * 9))  # Increased noise level
        return result * condition_factor + noise + 0.09 * np.sum(np.abs(x_norm)**8)  # Increased higher-order term