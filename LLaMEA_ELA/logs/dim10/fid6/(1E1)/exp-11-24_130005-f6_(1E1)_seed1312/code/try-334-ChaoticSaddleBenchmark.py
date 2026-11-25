import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic dynamics
        self.a = 1.4
        self.b = 0.3
        self.c = 0.5
        self.d = 0.8
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic saddle component with logistic map dynamics
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with parameter modulation
            r = 3.8 + 0.2 * np.sin(x_scaled[i] * 2.0)
            x_prev = np.sin(x_scaled[i] * 3.0) if i == 0 else x_scaled[i-1]
            chaotic += r * x_prev * (1 - x_prev)
        
        # Embedded periodic orbits with varying periods
        periodic = 0.0
        for i in range(self.dim):
            # Multiple periodic components with different periods and amplitudes
            period1 = 3 + int(2 * np.sin(x_scaled[i]))
            period2 = 5 + int(3 * np.cos(x_scaled[i]))
            
            orbit1 = np.sin(2 * np.pi * x_scaled[i] / period1) * np.cos(2 * np.pi * x_scaled[i] / period1)
            orbit2 = np.cos(2 * np.pi * x_scaled[i] / period2) * np.sin(2 * np.pi * x_scaled[i] / period2)
            
            periodic += 0.5 * (orbit1**2 + orbit2**2)
        
        # Gradient complexity with directional derivatives
        gradient = 0.0
        for i in range(self.dim):
            # Directional gradients with varying weights
            weight = 1.0 + 0.3 * np.sin(x_scaled[i] * 4.0)
            grad_term = weight * (np.sin(x_scaled[i]) + np.cos(x_scaled[i]))
            gradient += grad_term**2
        
        # Multi-scale harmonic interactions with phase shifts
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Phase-shifted harmonic interactions
                phase_shift = np.sin(0.5 * (x_scaled[i] + x_scaled[j]))
                harmonic += np.sin(x_scaled[i] * x_scaled[j] + phase_shift) * \
                           np.cos(x_scaled[i] - x_scaled[j]) * \
                           np.exp(-0.1 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Saddle point landscape with hyperbolic tangent transitions
        saddle = 0.0
        for i in range(self.dim):
            # Hyperbolic tangent transitions between regions
            tanh_term = np.tanh(5.0 * x_scaled[i])
            saddle += (tanh_term**2 - 0.5)**2
        
        # Combined function with modified weights
        return 0.7 * chaotic + 1.2 * periodic + 0.8 * gradient + 0.6 * harmonic + 0.9 * saddle