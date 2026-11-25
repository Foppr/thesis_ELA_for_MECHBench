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
            phase = np.sin(0.7 * x[i] + self.dim * 0.25) * np.cos(0.6 * x[i] + self.dim * 0.35)
            amplitude = 1.3 + 0.5 * np.sin(0.5 * x[i] + self.dim * 0.45)
            frequency = 2.8 + 1.2 * np.cos(0.6 * x[i] + 0.25 * self.dim)
            quantum += amplitude * np.sin(frequency * x[i] + phase) * np.exp(-0.09 * x[i]**2)
        
        # Enhanced time-varying chaotic attractors with adaptive coupling and modified weights
        chaotic = 0
        for i in range(self.dim):
            weight = 1.4 + 0.7 * np.sin(0.35 * x[i] + self.dim * 0.25)
            # Coupling with up to 5 nearest neighbors
            for j in range(max(0, i-4), min(i+5, self.dim)):
                if i != j:
                    distance = np.abs(x[i] - x[j])
                    coupling_factor = np.exp(-0.12 * distance**2)
                    chaotic += weight * coupling_factor * (x[i]**2 + x[j]**2)
        
        # Multi-scale oscillatory components with enhanced fractal frequency modulation
        oscillatory = 0
        for i in range(self.dim):
            freq1 = 2.2 + 0.9 * np.sin(0.35 * x[i])
            freq2 = 3.2 + 1.4 * np.cos(0.45 * x[i] + 0.12 * self.dim)
            freq3 = 4.2 + 1.8 * np.sin(0.55 * x[i] + 0.2 * self.dim)
            oscillatory += (np.sin(freq1 * x[i]) * 
                           np.cos(freq2 * x[i]**2) * 
                           np.sin(freq3 * x[i]**3) * 
                           np.exp(-0.12 * x[i]**2))
        
        # Enhanced adaptive ridge structures with modified exponential modulation
        ridges = 0
        for i in range(self.dim):
            height = 1.4 + 0.7 * np.sin(0.85 * x[i] + self.dim * 0.25)
            width = 0.9 + 0.25 * np.cos(0.65 * x[i])  # Modified width calculation
            ridge = height * np.exp(-0.45 * ((x[i] - 1.8) / width)**2)
            ridges += ridge
        
        # Dynamic conditioning with enhanced quantum-like tunneling behavior
        condition = 2.3 + 1.1 * np.sin(self.dim * 0.45 + 0.35 * np.cos(x[0] if self.dim > 0 else 0))
        
        # Asymmetric multimodal structure with enhanced quantum tunneling effects
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.45 * (x[i] - 2.3)**2) * np.sin(3.3 * x[i])
            term2 = np.exp(-0.45 * (x[i] + 2.3)**2) * np.cos(2.8 * x[i])
            term3 = np.exp(-0.35 * x[i]**2) * np.sin(4.2 * x[i]**2)
            # Enhanced quantum tunneling effect
            tunneling = 0.25 * np.sin(5.8 * x[i]) * np.exp(-0.12 * (x[i] - 0.6)**2)
            asymmetric += term1 + term2 + term3 + tunneling
        
        # Combine all components with modified weights and scaling
        return condition * (0.32 * quantum + 0.27 * chaotic + 
                           0.29 * oscillatory + 0.14 * ridges + 0.01 * asymmetric)