import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic saddle component with embedded periodic orbits
        chaotic = 0.0
        for i in range(self.dim):
            # Multi-scale chaotic dynamics with varying coupling strengths
            coupling = 0.5 + 0.3 * np.sin(i * 0.7)
            chaotic += coupling * np.sin(3.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[i])
            
        # Embedded periodic orbits with varying periods and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            period = 2.0 + 1.5 * np.sin(i * 0.5)
            amplitude = 1.2 + 0.8 * np.cos(i * 0.3)
            periodic += amplitude * np.sin(period * x_scaled[i]) * np.cos(period * x_scaled[i] * 0.5)
        
        # Multi-scale exponential decay with asymmetric fields
        decay = 0.0
        for i in range(self.dim):
            # Asymmetric decay rates based on position
            rate1 = 2.0 + 1.5 * np.sin(i * 0.8)
            rate2 = 1.5 + 1.0 * np.cos(i * 0.6)
            
            # Exponential decay with different rates for positive and negative regions
            if x_scaled[i] >= 0:
                decay += np.exp(-rate1 * x_scaled[i]) * np.sin(x_scaled[i])
            else:
                decay += np.exp(-rate2 * np.abs(x_scaled[i])) * np.cos(x_scaled[i])
        
        # Asymmetric gradient fields with directional preference
        gradient = 0.0
        for i in range(self.dim):
            # Directional bias based on dimension index
            bias = 0.5 + 0.3 * np.sin(i * 0.4)
            if x_scaled[i] >= 0:
                gradient += bias * x_scaled[i]**3
            else:
                gradient += (1.0 - bias) * x_scaled[i]**3
        
        # Cross-dimensional interaction terms with non-linear coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Non-linear interaction with varying coupling strength
                coupling = 1.0 + 0.5 * np.sin((i+j) * 0.3)
                cross += coupling * np.sin(x_scaled[i] * x_scaled[j]) * \
                        np.cos(0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Combined landscape with carefully balanced components
        return 1.2 * chaotic + 0.8 * periodic + 1.0 * decay + 0.6 * gradient + 0.9 * cross