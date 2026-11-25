import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced radial component with higher frequency harmonics and adaptive scaling
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1.0 + 0.4 * np.sin(7.0 * r) + 0.3 * np.cos(9.0 * r) + 0.2 * np.sin(11.0 * r))
        
        # Improved gradient-based chaotic perturbations with exponential decay
        grad_term = 0.0
        for i in range(self.dim):
            # Directional gradient with enhanced chaotic modulation
            direction = x_scaled[i] / (np.abs(x_scaled[i]) + 1e-8)
            grad_pert = 2.5 * np.sin(4.0 * x_scaled[i] + 2.0 * r) * np.cos(3.0 * x_scaled[i]) * np.exp(-0.3 * r)
            grad_term += direction * grad_pert
            
        # Enhanced multi-scale harmonic interactions with asymmetric coupling
        harmonic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric cross-dimensional harmonic coupling
                coupling = np.sin(3.0 * x_scaled[i] + 2.0 * x_scaled[j]) * np.cos(1.5 * x_scaled[i] - x_scaled[j])
                distance = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.05)
                harmonic_term += coupling / (distance + 0.05) * np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Modified chaotic sine-wave modulation with frequency-dependent damping
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 5.0 + 3.0 * np.sin(2.0 * x_scaled[i])
            chaotic_term += np.sin(freq * x_scaled[i]) * np.cos(4.0 * x_scaled[i]) * np.exp(-0.4 * x_scaled[i]**2)
        
        # Enhanced nested oscillatory components with varying frequencies and amplitudes
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += (0.6 * np.sin(12.0 * x_scaled[i]) + 
                           0.4 * np.sin(30.0 * x_scaled[i]) + 
                           0.3 * np.sin(60.0 * x_scaled[i]) + 
                           0.2 * np.sin(80.0 * x_scaled[i]))
        
        # Combined landscape with adjusted weights for better conditioning
        return 0.9 * radial_term + 0.7 * grad_term + 0.5 * harmonic_term + 0.8 * chaotic_term + 0.6 * nested_term + 2.5