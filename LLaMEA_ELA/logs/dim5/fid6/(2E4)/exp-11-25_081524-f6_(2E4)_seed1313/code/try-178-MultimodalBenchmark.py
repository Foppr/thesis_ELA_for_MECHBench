import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute time-varying parameters for dynamic behavior
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.02  # Increment time for dynamic effects
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with enhanced non-linearity
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 4.0 + 2.0 * np.sin(0.5 * self.t + i * 0.8)
            amp = 2.0 + 0.8 * np.cos(0.4 * self.t + i * 0.6)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.tanh(x[i])
        
        # Enhanced adaptive penalty regions with exponential scaling
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                penalty += 25.0 * np.exp(3.0 * (abs(x[i]) - 4.5))
            elif abs(x[i]) < 0.1:
                penalty += 15.0 * (0.1 - abs(x[i]))**4
        
        # Multi-scale fractal interference with dynamic coupling and phase modulation
        fractal_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):  # Increased coupling range
                coupling_strength = 0.9 + 0.4 * np.sin(0.6 * self.t + i * 0.5 + j * 0.4)
                phase_shift = 0.3 * np.cos(0.4 * self.t + i * 0.3 + j * 0.2)
                dist = np.abs(x[i] - x[j])
                fractal_interference += coupling_strength * np.exp(-dist**2) * np.sin(4.0 * dist + phase_shift)
        
        # Time-varying harmonic potentials with stochastic amplitude modulation
        harmonic_potential = 0.0
        for i in range(self.dim):
            amp = 2.0 + 0.6 * np.sin(0.7 * self.t + i * 0.6) * np.cos(0.5 * self.t + i * 0.4)
            phase = 0.4 * np.sin(0.6 * self.t + i * 0.3) + 0.2 * np.cos(0.4 * self.t + i * 0.2)
            harmonic_potential += amp * (x[i]**4) * np.cos(phase + x[i]**3)
        
        # Polynomial scaling with enhanced dimensionality dependence
        poly_scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.03 * self.dim**0.8 if self.dim > 0 else 1.0
        
        # Dynamic weights with higher frequency modulation for increased complexity
        weight1 = 0.5 + 0.25 * np.sin(0.6 * self.t)
        weight2 = 0.4 + 0.2 * np.cos(0.5 * self.t)
        weight3 = 0.3 + 0.2 * np.sin(0.7 * self.t)
        
        result = weight1 * chaotic_grad + weight2 * fractal_interference + weight3 * harmonic_potential + penalty
        return result * poly_scale