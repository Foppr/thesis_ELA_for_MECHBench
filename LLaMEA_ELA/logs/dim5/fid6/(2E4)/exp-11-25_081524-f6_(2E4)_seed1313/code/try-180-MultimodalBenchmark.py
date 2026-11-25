import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute time-varying parameters for dynamic behavior
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.01  # Increment time for dynamic effects
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with enhanced non-linearity
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 3.2 + 1.3 * np.sin(0.42 * self.t + i * 0.73)
            amp = 1.6 + 0.4 * np.cos(0.31 * self.t + i * 0.52)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.tanh(x[i])
        
        # Enhanced adaptive penalty regions with exponential scaling
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.1:
                penalty += 16.0 * np.exp(2.1 * (abs(x[i]) - 4.1))
            elif abs(x[i]) < 0.2:
                penalty += 8.5 * (0.2 - abs(x[i]))**3
        
        # Multi-scale fractal interference with dynamic coupling and phase modulation
        fractal_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Slightly reduced coupling for scalability
                coupling_strength = 0.65 + 0.35 * np.sin(0.52 * self.t + i * 0.42 + j * 0.32)
                phase_shift = 0.22 * np.cos(0.32 * self.t + i * 0.22 + j * 0.12)
                dist = np.abs(x[i] - x[j])
                fractal_interference += coupling_strength * np.exp(-dist**2) * np.sin(3.2 * dist + phase_shift)
        
        # Time-varying harmonic potentials with stochastic amplitude modulation
        harmonic_potential = 0.0
        for i in range(self.dim):
            amp = 1.25 + 0.45 * np.sin(0.61 * self.t + i * 0.51) * np.cos(0.41 * self.t + i * 0.31)
            phase = 0.31 * np.sin(0.51 * self.t + i * 0.21) + 0.11 * np.cos(0.31 * self.t + i * 0.11)
            harmonic_potential += amp * (x[i]**3) * np.cos(phase + x[i]**2)
        
        # Polynomial scaling with enhanced dimensionality dependence
        poly_scale = 1.0 + 0.16 * np.log(self.dim + 1) + 0.022 * self.dim**0.7 if self.dim > 0 else 1.0
        
        # Dynamic weights with higher frequency modulation for increased complexity
        weight1 = 0.42 + 0.18 * np.sin(0.51 * self.t)
        weight2 = 0.36 + 0.19 * np.cos(0.41 * self.t)
        weight3 = 0.24 + 0.16 * np.sin(0.61 * self.t)
        
        result = weight1 * chaotic_grad + weight2 * fractal_interference + weight3 * harmonic_potential + penalty
        return result * poly_scale