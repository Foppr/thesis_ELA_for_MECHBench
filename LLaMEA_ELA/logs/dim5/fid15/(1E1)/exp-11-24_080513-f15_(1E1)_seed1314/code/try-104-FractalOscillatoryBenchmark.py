import numpy as np

class FractalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic dynamical system component with logistic map coupling
        chaotic = 0.0
        r = 3.99
        x_prev = 0.5
        for i in range(self.dim):
            x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_prev * 10 * np.pi) * np.cos(x_normalized[i] * 7.0) * np.exp(-0.5 * x_normalized[i]**2)
        
        # Fractal geometric component with multi-dimensional Cantor set patterns
        fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                fractal += (np.sin(2**j * x_normalized[i]) * np.cos(3**i * x_normalized[j])) / (1.0 + dist**2)
        
        # Quantum-like interference patterns with complex phase modulation
        quantum = 0.0
        for i in range(self.dim):
            phase = np.sin(x_normalized[i] * np.pi) * np.cos(x_normalized[i] * 2 * np.pi)
            amplitude = np.exp(-0.5 * x_normalized[i]**2) * (1.0 + 0.3 * np.sin(x_normalized[i] * 5))
            quantum += amplitude * np.sin(15 * x_normalized[i] + phase) * np.cos(15 * x_normalized[i] + phase)
        
        # Multi-scale radial basis with logarithmic spacing and exponential weighting
        radial = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.2) * np.cos(i * 0.3) * np.exp(-i * 0.1)
            width = 0.1 + 0.4 * np.sin(i * 0.5)**2
            radial += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2) * np.log(1.0 + i * 0.1)
        
        # Cross-dimensional coupling with fractional Brownian motion characteristics
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                strength = 0.8 * np.sin(i * 0.3) * np.cos(j * 0.4)
                coupling += strength * np.exp(-dist**2) * np.sin(10 * dist) * (1.0 + 0.2 * np.sin(dist * 3))
        
        # Polynomial interaction with prime number-based exponents
        poly = 0.0
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                prime_idx = (i + j) % len(primes)
                poly += (x_normalized[i] * x_normalized[j])**(primes[prime_idx])
        
        # Hyperbolic tangent oscillatory component with varying frequency modulation
        hyperbolic = 0.0
        for i in range(self.dim):
            freq = 20.0 + 10.0 * np.tanh(i * 0.3)
            amp = 1.0 / (1.0 + 0.5 * np.exp(-i * 0.2))
            hyperbolic += amp * np.tanh(freq * x_normalized[i]) * np.sin(freq * x_normalized[i])
        
        # Logarithmic noise with chaotic seed and multi-dimensional correlation
        noise = 0.0
        for i in range(self.dim):
            seed = np.sin(i * 1.7) * np.cos(i * 2.3)
            noise += np.log(1.0 + 0.5 * x_normalized[i]**2) * np.sin(25 * x_normalized[i] + seed)
        
        # Combine all components with adaptive weights and non-linear scaling
        return (0.25 * chaotic + 0.2 * fractal + 0.15 * quantum + 
                0.1 * radial + 0.1 * coupling + 0.08 * poly + 0.07 * hyperbolic + 0.05 * noise)