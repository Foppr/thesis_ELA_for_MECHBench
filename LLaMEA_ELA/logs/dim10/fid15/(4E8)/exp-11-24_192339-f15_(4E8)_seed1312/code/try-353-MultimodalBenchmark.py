import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired superposition states with dynamic phase interference
        quantum = 0
        for i in range(self.dim):
            phase = np.sin(0.7 * x[i] + self.dim * 0.15) * np.cos(0.4 * x[i] + self.dim * 0.2)
            amplitude = 1.0 + 0.4 * np.sin(0.5 * x[i] + self.dim * 0.3)
            frequency = 2.0 + 1.2 * np.cos(0.6 * x[i] + 0.2 * self.dim)
            quantum += amplitude * np.sin(frequency * x[i] + phase) * np.exp(-0.05 * x[i]**2)
        
        # Time-varying chaotic attractors with adaptive coupling
        chaotic = 0
        for i in range(self.dim):
            # Adaptive weight based on position and dimension
            weight = 1.0 + 0.6 * np.sin(0.3 * x[i] + self.dim * 0.2)
            # Coupling with up to 3 nearest neighbors
            for j in range(max(0, i-2), min(i+3, self.dim)):
                if i != j:
                    distance = np.abs(x[i] - x[j])
                    coupling_factor = np.exp(-0.1 * distance**2)
                    chaotic += weight * coupling_factor * (x[i]**2 + x[j]**2)
        
        # Multi-scale oscillatory components with fractal frequency modulation
        oscillatory = 0
        for i in range(self.dim):
            freq1 = 1.5 + 0.8 * np.sin(0.3 * x[i])
            freq2 = 2.5 + 1.0 * np.cos(0.4 * x[i] + 0.1 * self.dim)
            freq3 = 3.5 + 1.5 * np.sin(0.5 * x[i] + 0.2 * self.dim)
            oscillatory += (np.sin(freq1 * x[i]) * 
                           np.cos(freq2 * x[i]**2) * 
                           np.sin(freq3 * x[i]**3) * 
                           np.exp(-0.1 * x[i]**2))
        
        # Adaptive ridge structures with exponential modulation
        ridges = 0
        for i in range(self.dim):
            # Ridge structure with varying heights and widths
            height = 1.0 + 0.5 * np.sin(0.8 * x[i] + self.dim * 0.25)
            width = 0.5 + 0.3 * np.cos(0.6 * x[i])
            ridge = height * np.exp(-0.5 * ((x[i] - 1.5) / width)**2)
            ridges += ridge
        
        # Dynamic conditioning with quantum-like tunneling behavior
        condition = 2.0 + 0.8 * np.sin(self.dim * 0.4 + 0.3 * np.cos(x[0] if self.dim > 0 else 0))
        
        # Asymmetric multimodal structure with quantum tunneling effects
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(3.0 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(2.5 * x[i])
            term3 = np.exp(-0.3 * x[i]**2) * np.sin(4.0 * x[i]**2)
            # Quantum tunneling effect
            tunneling = 0.2 * np.sin(5.0 * x[i]) * np.exp(-0.1 * (x[i] - 0.5)**2)
            asymmetric += term1 + term2 + term3 + tunneling
        
        # Combine all components with optimized weights and scaling
        return condition * (0.28 * quantum + 0.22 * chaotic + 
                           0.25 * oscillatory + 0.20 * ridges + 0.05 * asymmetric)