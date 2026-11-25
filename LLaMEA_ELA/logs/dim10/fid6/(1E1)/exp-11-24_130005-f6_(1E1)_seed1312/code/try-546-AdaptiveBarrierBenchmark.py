import numpy as np

class AdaptiveBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic trigonometric components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.5 + 0.5 * np.cos(i * 0.3)
            periodic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Exponential barrier functions with adaptive widths and heights
        barriers = 0.0
        for i in range(self.dim):
            # Multiple exponential barriers around different positions
            pos1 = 0.2 * np.sin(i * 0.4)
            pos2 = -0.3 * np.cos(i * 0.6)
            width1 = 0.5 + 0.3 * np.sin(i * 0.8)
            width2 = 0.4 + 0.2 * np.cos(i * 0.5)
            
            barrier1 = np.exp(-0.5 * ((x_scaled[i] - pos1) / width1)**2)
            barrier2 = np.exp(-0.5 * ((x_scaled[i] - pos2) / width2)**2)
            barriers += barrier1 + barrier2
        
        # Adaptive conditioning with dimension-dependent scaling
        conditioning = 0.0
        for i in range(self.dim):
            # Varying conditioning based on dimension index and input value
            cond_factor = 1.0 + 2.0 * np.sin(i * 0.3 + x_scaled[i] * 0.5)
            conditioning += cond_factor * x_scaled[i]**2
        
        # Cross-dimensional interaction with trigonometric coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling += np.sin(x_scaled[i] + x_scaled[j]) * \
                           np.cos(x_scaled[i] - x_scaled[j]) * \
                           np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Multi-scale oscillatory components with varying amplitudes and frequencies
        oscillatory = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            for i in range(self.dim):
                oscillatory += (scale * np.sin(scale * x_scaled[i]) * 
                               np.cos(scale * x_scaled[i] * 0.8) * 
                               np.exp(-0.1 * scale * np.abs(x_scaled[i])))
        
        # Asymmetric landscape with exponential decay and sharp gradients
        asymmetry = 0.0
        for i in range(self.dim):
            # Create asymmetric regions using exponential terms with different decay rates
            asymmetry += (np.exp(-2.0 * (x_scaled[i] - 0.3)**2) - 
                         np.exp(-1.5 * (x_scaled[i] + 0.3)**2))
        
        # Combine all components with carefully tuned weights for maximum challenge
        return 1.5 * periodic + 2.0 * barriers + 1.2 * conditioning + 0.8 * coupling + 1.0 * oscillatory + 0.9 * asymmetry