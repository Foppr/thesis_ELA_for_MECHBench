import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle point dynamics with multi-scale modulation
        chaotic = 0
        for i in range(self.dim):
            well1 = np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(4.0 * x[i])
            well2 = np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(3.0 * x[i])
            phase_mod = 1.0 + 0.5 * np.sin(0.3 * x[i] + self.dim * 0.4)
            saddle = (well1 + well2) * phase_mod
            chaotic += saddle
        
        # Fractal ridge coupling with dynamic scaling and interference
        coupling = 0
        for i in range(self.dim):
            for j in range(max(0, i-2), min(i+3, self.dim)):
                if i != j:
                    coupling_strength = 1.2 * np.exp(-0.3 * (i - j)**2) * (1.0 + 0.3 * np.sin(0.4 * x[i] + 0.5 * x[j]))
                    distance = np.abs(x[i] - x[j])
                    coupling_factor = 1.0 / (1.0 + np.exp(1.5 * distance))
                    ridge_mod = 1.0 + 0.4 * np.cos(0.6 * x[i] + 0.3 * self.dim)
                    coupling += coupling_strength * coupling_factor * (x[i]**2 + x[j]**2) * ridge_mod
        
        # Quantum-inspired oscillatory components with dynamic tunneling
        oscillatory = 0
        for i in range(self.dim):
            freq1 = 2.5 + 1.5 * np.sin(0.5 * x[i])
            freq2 = 3.5 + 2.0 * np.cos(0.6 * x[i] + 0.2 * self.dim)
            freq3 = 4.5 + 2.5 * np.sin(0.7 * x[i] + 0.3 * self.dim)
            tunneling_prob = 0.6 + 0.4 * np.sin(0.8 * x[i] + self.dim * 0.2)
            oscillatory += (np.sin(freq1 * x[i]) * 
                           np.cos(freq2 * x[i]**2) * 
                           np.sin(freq3 * x[i]**3) * 
                           tunneling_prob * 
                           np.exp(-0.2 * x[i]**2))
        
        # Asymmetric multimodal with enhanced chaotic interference
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 1.2)**2) * np.sin(5.5 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 1.2)**2) * np.cos(4.5 * x[i])
            term3 = np.exp(-0.35 * x[i]**2) * np.sin(6.5 * x[i]**2)
            phase_interference = np.sin(1.0 * x[i] + self.dim * 0.35)
            asymmetric += (term1 + term2 + term3) * (1.0 + 0.5 * phase_interference)
        
        # Dynamic conditioning with chaotic scaling factor
        condition = 2.0 + 0.8 * np.sin(0.7 * x[0] + self.dim * 0.3)
        
        # Combine all components with optimized weights for improved performance
        return condition * (0.30 * chaotic + 0.25 * coupling + 
                           0.20 * oscillatory + 0.15 * asymmetric)