import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired superposition with dynamic phase modulation and multi-frequency interference
        quantum = 0
        for i in range(self.dim):
            phase1 = np.sin(0.9 * x[i] + self.dim * 0.25)
            phase2 = np.cos(0.6 * x[i] + self.dim * 0.35)
            amplitude = 1.3 + 0.7 * np.sin(0.7 * x[i] + self.dim * 0.45)
            frequency1 = 2.8 + 1.8 * np.cos(0.8 * x[i] + 0.4 * self.dim)
            frequency2 = 3.2 + 2.0 * np.sin(0.6 * x[i] + 0.3 * self.dim)
            quantum += amplitude * (np.sin(frequency1 * x[i] + phase1) * 
                                   np.cos(frequency2 * x[i] + phase2)) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced chaotic attractors with multi-scale coupling and dynamic weights
        chaotic = 0
        for i in range(self.dim):
            weight = 1.7 + 0.9 * np.sin(0.5 * x[i] + self.dim * 0.35)
            # Coupling with up to 5 nearest neighbors
            for j in range(max(0, i-4), min(i+5, self.dim)):
                if i != j:
                    distance = np.abs(x[i] - x[j])
                    coupling_factor = np.exp(-0.2 * distance**2)
                    chaotic += weight * coupling_factor * (x[i]**2 + x[j]**2)
        
        # Multi-scale oscillatory components with fractal frequency modulation and enhanced amplitude
        oscillatory = 0
        for i in range(self.dim):
            freq1 = 2.2 + 1.2 * np.sin(0.5 * x[i])
            freq2 = 3.5 + 1.8 * np.cos(0.6 * x[i] + 0.2 * self.dim)
            freq3 = 4.5 + 2.5 * np.sin(0.7 * x[i] + 0.3 * self.dim)
            oscillatory += (np.sin(freq1 * x[i]) * 
                           np.cos(freq2 * x[i]**2) * 
                           np.sin(freq3 * x[i]**3) * 
                           np.exp(-0.2 * x[i]**2))
        
        # Enhanced adaptive ridge structures with exponential modulation and asymmetric scaling
        ridges = 0
        for i in range(self.dim):
            height = 1.8 + 0.9 * np.sin(1.0 * x[i] + self.dim * 0.35)
            width = 0.9 + 0.4 * np.cos(0.8 * x[i])
            ridge = height * np.exp(-0.4 * ((x[i] - 2.2) / width)**2)
            ridges += ridge
        
        # Dynamic conditioning with quantum-like tunneling behavior and time-varying scaling
        condition = 3.0 + 1.5 * np.sin(self.dim * 0.6 + 0.5 * np.cos(x[0] if self.dim > 0 else 0))
        
        # Asymmetric multimodal structure with enhanced quantum tunneling and cross-dimensional coupling
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.6 * (x[i] - 2.8)**2) * np.sin(4.0 * x[i])
            term2 = np.exp(-0.6 * (x[i] + 2.8)**2) * np.cos(3.5 * x[i])
            term3 = np.exp(-0.5 * x[i]**2) * np.sin(5.0 * x[i]**2)
            # Enhanced quantum tunneling effect with dynamic scaling
            tunneling = 0.4 * np.sin(7.0 * x[i]) * np.exp(-0.2 * (x[i] - 0.8)**2)
            asymmetric += term1 + term2 + term3 + tunneling
        
        # Combine all components with increased weights and scaling
        return condition * (0.35 * quantum + 0.30 * chaotic + 
                           0.25 * oscillatory + 0.18 * ridges + 0.02 * asymmetric)