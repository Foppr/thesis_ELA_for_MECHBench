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
            freq = 4.0 + 2.0 * np.sin(0.5 * self.t + i * 0.8)
            amp = 2.0 + 0.8 * np.cos(0.4 * self.t + i * 0.6)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.tanh(x[i]) + 0.15 * x[i]**4 + 0.05 * x[i]**6
        
        # Enhanced adaptive penalty regions with exponential scaling and additional quadratic term
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.3:
                penalty += 20.0 * np.exp(2.5 * (abs(x[i]) - 4.3)) + 3.0 * (abs(x[i]) - 4.3)**2 + 0.5 * (abs(x[i]) - 4.3)**4
            elif abs(x[i]) < 0.2:
                penalty += 10.0 * (0.2 - abs(x[i]))**3 + 2.0 * (0.2 - abs(x[i]))**2 + 0.3 * (0.2 - abs(x[i]))**5
        
        # Multi-scale fractal interference with dynamic coupling and phase modulation, extended range
        fractal_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+15, self.dim)):  # Increased coupling range for higher complexity
                coupling_strength = 0.8 + 0.4 * np.sin(0.6 * self.t + i * 0.5 + j * 0.4)
                phase_shift = 0.3 * np.cos(0.4 * self.t + i * 0.3 + j * 0.2)
                dist = np.abs(x[i] - x[j])
                fractal_interference += coupling_strength * np.exp(-dist**2) * np.sin(4.0 * dist + phase_shift) + 0.08 * np.cos(6.0 * dist) + 0.03 * np.sin(7.0 * dist)
        
        # Time-varying harmonic potentials with stochastic amplitude modulation and additional cubic terms
        harmonic_potential = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.5 * np.sin(0.7 * self.t + i * 0.6) * np.cos(0.5 * self.t + i * 0.4)
            phase = 0.4 * np.sin(0.6 * self.t + i * 0.3) + 0.2 * np.cos(0.4 * self.t + i * 0.2)
            harmonic_potential += amp * (x[i]**3) * np.cos(phase + x[i]**2) + 0.25 * x[i]**5 + 0.1 * x[i]**7
        
        # Polynomial scaling with enhanced dimensionality dependence and additional logarithmic term
        poly_scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.03 * self.dim**0.8 + 0.008 * np.log(self.dim + 1)**2 + 0.005 * self.dim**0.5 if self.dim > 0 else 1.0
        
        # Dynamic weights with higher frequency modulation for increased complexity
        weight1 = 0.45 + 0.25 * np.sin(0.6 * self.t) + 0.07 * np.cos(0.8 * self.t)
        weight2 = 0.38 + 0.22 * np.cos(0.5 * self.t) + 0.04 * np.sin(0.7 * self.t)
        weight3 = 0.27 + 0.19 * np.sin(0.7 * self.t) + 0.05 * np.cos(0.9 * self.t)
        
        result = weight1 * chaotic_grad + weight2 * fractal_interference + weight3 * harmonic_potential + penalty
        return result * poly_scale