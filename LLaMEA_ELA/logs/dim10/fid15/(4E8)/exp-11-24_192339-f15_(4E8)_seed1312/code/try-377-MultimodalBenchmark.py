import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quantum-inspired superposition states with time-varying phase interference
        quantum = 0
        for i in range(self.dim):
            phase = np.sin(0.8 * x[i] + self.dim * 0.2) * np.cos(0.5 * x[i] + self.dim * 0.3)
            amplitude = 1.2 + 0.6 * np.sin(0.6 * x[i] + self.dim * 0.4)
            frequency = 2.5 + 1.5 * np.cos(0.7 * x[i] + 0.3 * self.dim)
            quantum += amplitude * np.sin(frequency * x[i] + phase) * np.exp(-0.08 * x[i]**2)
        
        # Enhanced time-varying chaotic attractors with adaptive coupling and modified weights
        chaotic = 0
        for i in range(self.dim):
            weight = 1.5 + 0.8 * np.sin(0.4 * x[i] + self.dim * 0.3)
            # Coupling with up to 4 nearest neighbors
            for j in range(max(0, i-3), min(i+4, self.dim)):
                if i != j:
                    distance = np.abs(x[i] - x[j])
                    coupling_factor = np.exp(-0.15 * distance**2)
                    chaotic += weight * coupling_factor * (x[i]**2 + x[j]**2)
        
        # Multi-scale oscillatory components with enhanced fractal frequency modulation
        oscillatory = 0
        for i in range(self.dim):
            freq1 = 2.0 + 1.0 * np.sin(0.4 * x[i])
            freq2 = 3.0 + 1.5 * np.cos(0.5 * x[i] + 0.15 * self.dim)
            freq3 = 4.0 + 2.0 * np.sin(0.6 * x[i] + 0.25 * self.dim)
            oscillatory += (np.sin(freq1 * x[i]) * 
                           np.cos(freq2 * x[i]**2) * 
                           np.sin(freq3 * x[i]**3) * 
                           np.exp(-0.15 * x[i]**2))
        
        # Enhanced adaptive ridge structures with modified exponential modulation
        ridges = 0
        for i in range(self.dim):
            height = 1.5 + 0.8 * np.sin(0.9 * x[i] + self.dim * 0.3)
            width = 0.8 + 0.3 * np.cos(0.7 * x[i])  # Modified width calculation
            ridge = height * np.exp(-0.5 * ((x[i] - 2.0) / width)**2)
            ridges += ridge
        
        # Dynamic conditioning with enhanced quantum-like tunneling behavior
        condition = 2.5 + 1.0 * np.sin(self.dim * 0.5 + 0.4 * np.cos(x[0] if self.dim > 0 else 0))
        
        # Asymmetric multimodal structure with enhanced quantum tunneling effects
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 2.5)**2) * np.sin(3.5 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 2.5)**2) * np.cos(3.0 * x[i])
            term3 = np.exp(-0.4 * x[i]**2) * np.sin(4.5 * x[i]**2)
            # Enhanced quantum tunneling effect
            tunneling = 0.3 * np.sin(6.0 * x[i]) * np.exp(-0.15 * (x[i] - 0.7)**2)
            asymmetric += term1 + term2 + term3 + tunneling
        
        # Combine all components with modified weights and scaling
        return condition * (0.30 * quantum + 0.25 * chaotic + 
                           0.28 * oscillatory + 0.15 * ridges + 0.02 * asymmetric)