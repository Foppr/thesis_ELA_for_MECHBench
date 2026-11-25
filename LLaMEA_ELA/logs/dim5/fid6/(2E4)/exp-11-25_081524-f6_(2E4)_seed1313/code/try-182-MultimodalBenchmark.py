import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute time-varying parameters for dynamic behavior
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.01  # Increment time for dynamic effects
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with enhanced non-linearity and higher-order terms
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(0.4 * self.t + i * 0.7)
            amp = 1.5 + 0.5 * np.cos(0.3 * self.t + i * 0.5)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.tanh(x[i]) + 0.1 * x[i]**4
        
        # Enhanced adaptive penalty regions with exponential scaling and additional quadratic term
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.2:
                penalty += 15.0 * np.exp(2.0 * (abs(x[i]) - 4.2)) + 2.0 * (abs(x[i]) - 4.2)**2
            elif abs(x[i]) < 0.25:
                penalty += 8.0 * (0.25 - abs(x[i]))**3 + 1.5 * (0.25 - abs(x[i]))**2
        
        # Multi-scale fractal interference with dynamic coupling and phase modulation, extended range
        fractal_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):  # Extended coupling range for higher complexity
                coupling_strength = 0.7 + 0.3 * np.sin(0.5 * self.t + i * 0.4 + j * 0.3)
                phase_shift = 0.2 * np.cos(0.3 * self.t + i * 0.2 + j * 0.1)
                dist = np.abs(x[i] - x[j])
                fractal_interference += coupling_strength * np.exp(-dist**2) * np.sin(3.0 * dist + phase_shift) + 0.05 * np.cos(5.0 * dist)
        
        # Time-varying harmonic potentials with stochastic amplitude modulation and additional cubic terms
        harmonic_potential = 0.0
        for i in range(self.dim):
            amp = 1.3 + 0.4 * np.sin(0.6 * self.t + i * 0.5) * np.cos(0.4 * self.t + i * 0.3)
            phase = 0.3 * np.sin(0.5 * self.t + i * 0.2) + 0.1 * np.cos(0.3 * self.t + i * 0.1)
            harmonic_potential += amp * (x[i]**3) * np.cos(phase + x[i]**2) + 0.2 * x[i]**5
        
        # Polynomial scaling with enhanced dimensionality dependence and additional logarithmic term
        poly_scale = 1.0 + 0.15 * np.log(self.dim + 1) + 0.02 * self.dim**0.7 + 0.005 * np.log(self.dim + 1)**2 if self.dim > 0 else 1.0
        
        # Dynamic weights with higher frequency modulation for increased complexity
        weight1 = 0.4 + 0.2 * np.sin(0.5 * self.t) + 0.05 * np.cos(0.7 * self.t)
        weight2 = 0.35 + 0.18 * np.cos(0.4 * self.t) + 0.03 * np.sin(0.6 * self.t)
        weight3 = 0.25 + 0.17 * np.sin(0.6 * self.t) + 0.04 * np.cos(0.8 * self.t)
        
        result = weight1 * chaotic_grad + weight2 * fractal_interference + weight3 * harmonic_potential + penalty
        return result * poly_scale