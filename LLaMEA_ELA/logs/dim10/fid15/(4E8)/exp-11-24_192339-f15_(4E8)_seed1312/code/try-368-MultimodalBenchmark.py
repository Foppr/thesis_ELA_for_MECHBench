import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic saddle point with dynamic basin boundaries
        chaotic = 0
        for i in range(self.dim):
            # Saddle point with time-varying potential wells
            well1 = np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(4.0 * x[i])
            well2 = np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(3.0 * x[i])
            saddle = well1 + well2
            # Dynamic basin modulation with fractal scaling
            basin_mod = 1.0 + 0.3 * np.sin(0.5 * x[i] + self.dim * 0.4)
            chaotic += basin_mod * saddle
        
        # Enhanced non-separability through fractal coupling
        coupling = 0
        for i in range(self.dim):
            # Multi-scale coupling with fractal dimensionality
            for j in range(max(0, i-3), min(i+4, self.dim)):
                if i != j:
                    # Fractal coupling strength with exponential decay
                    coupling_strength = 1.5 * np.exp(-0.2 * (i - j)**2) * (1.0 + 0.2 * np.sin(0.3 * x[i] + 0.4 * x[j]))
                    distance = np.abs(x[i] - x[j])
                    coupling_factor = 1.0 / (1.0 + np.exp(2.0 * distance))
                    coupling += coupling_strength * coupling_factor * (x[i]**2 + x[j]**2)
        
        # Dynamic ridge structures with chaotic modulation
        ridges = 0
        for i in range(self.dim):
            # Chaotic ridge height and width modulation
            height = 1.5 + 0.8 * np.sin(0.7 * x[i] + self.dim * 0.3)
            width = 0.8 + 0.4 * np.cos(0.6 * x[i] + 0.2 * self.dim)
            # Saddle point ridge with chaotic phase
            phase = np.sin(0.8 * x[i] + self.dim * 0.5)
            ridge = height * np.exp(-0.5 * ((x[i] - 1.0) / width)**2) * (1.0 + 0.3 * phase)
            ridges += ridge
        
        # Multi-scale oscillatory components with quantum tunneling
        oscillatory = 0
        for i in range(self.dim):
            # Fractal frequency modulation with multiple scales
            freq1 = 2.0 + 1.0 * np.sin(0.4 * x[i])
            freq2 = 3.0 + 1.5 * np.cos(0.5 * x[i] + 0.1 * self.dim)
            freq3 = 4.0 + 2.0 * np.sin(0.6 * x[i] + 0.2 * self.dim)
            # Quantum tunneling effect with dynamic probability
            tunneling_prob = 0.5 + 0.3 * np.sin(0.7 * x[i])
            oscillatory += (np.sin(freq1 * x[i]) * 
                           np.cos(freq2 * x[i]**2) * 
                           np.sin(freq3 * x[i]**3) * 
                           tunneling_prob * 
                           np.exp(-0.15 * x[i]**2))
        
        # Asymmetric multimodal with chaotic phase interference
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 1.5)**2) * np.sin(5.0 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 1.5)**2) * np.cos(4.0 * x[i])
            term3 = np.exp(-0.3 * x[i]**2) * np.sin(6.0 * x[i]**2)
            # Chaotic phase interference
            phase_interference = np.sin(0.9 * x[i] + self.dim * 0.3)
            asymmetric += (term1 + term2 + term3) * (1.0 + 0.4 * phase_interference)
        
        # Dynamic conditioning with chaotic scaling
        condition = 1.5 + 0.7 * np.sin(0.6 * x[0] + self.dim * 0.25)
        
        # Combine all components with modified weights for increased complexity
        return condition * (0.25 * chaotic + 0.25 * coupling + 
                           0.20 * ridges + 0.20 * oscillatory + 0.10 * asymmetric)