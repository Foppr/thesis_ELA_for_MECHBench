import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize quaternion-based chaotic parameters for hyper-chaos
        self.q_params = np.array([3.9 + 0.2 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)])
        self.freq_mod = np.array([1.0 + 0.5 * np.cos(i * np.pi / (dim + 1)) for i in range(dim)])
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Fractal component using quaternion-inspired cosine patterns with phase shifts
        fractal_sum = 0.0
        scales = [1, 2, 3, 4, 6]
        for scale in scales:
            for i in range(self.dim):
                xi = x_scaled[i]
                freq = scale * (i + 1) * self.freq_mod[i] * np.pi / (self.dim + 1)
                phase_shift = np.sin(scale * i * np.pi / (self.dim + 1))
                fractal_sum += np.cos(freq * xi + phase_shift) * np.exp(-0.3 * (xi**2) / scale)
        
        # Hyper-chaotic component using quaternion-based logistic maps
        chaotic_sum = 0.0
        x_logistic = 0.5 * np.ones(self.dim)
        for t in range(15):  # More iterations for stronger chaos
            for i in range(self.dim):
                r = self.q_params[i]
                x_logistic[i] = r * x_logistic[i] * (1 - x_logistic[i])
        
        for i in range(self.dim):
            chaotic_sum += x_logistic[i] * np.sin((i + 1) * np.pi * x_scaled[i]) * np.cos(x_scaled[i]**2)
        
        # Cross-dimensional interaction with exponential barriers
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_scaled[i] - x_scaled[j])
                # Exponential barrier weighting
                weight = np.exp(-0.5 * dist**2) / (1 + 0.2 * dist**4)
                interaction += weight * np.sin(3 * (x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] * x_scaled[j]))
        
        # Multi-modal component with dynamic amplitude modulation
        modal_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Dynamic amplitudes based on dimension index
            amp1, amp2, amp3 = 0.6 * (1 + 0.2 * np.sin(i)), 0.4 * (1 + 0.3 * np.cos(i)), 0.2 * (1 + 0.1 * np.sin(2*i))
            modal_component += (amp1 * np.sin(15 * xi) + amp2 * np.sin(25 * xi) + 
                              amp3 * np.sin(40 * xi)) * np.exp(-0.15 * xi**2)
        
        # Add exponential decay barriers to encourage boundary exploration
        barrier_penalty = 0.0
        for i in range(self.dim):
            barrier_penalty += np.exp(-2.0 * (abs(x_scaled[i]) - 0.8)**2) * (1 - abs(x_scaled[i]))
        
        # Combine all components with adaptive weights based on dimensionality
        dim_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        return dim_factor * (0.5 * fractal_sum + 0.25 * chaotic_sum + 
                           0.3 * interaction + 0.35 * modal_component) + 2.0 * barrier_penalty