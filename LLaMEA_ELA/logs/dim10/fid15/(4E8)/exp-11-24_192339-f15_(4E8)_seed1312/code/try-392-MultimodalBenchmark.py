import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic saddle point with dynamic basin boundaries
        chaotic = 0
        for i in range(self.dim):
            # Saddle point with time-varying potential wells and phase modulation
            well1 = np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(4.0 * x[i] + 0.5 * self.dim)
            well2 = np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(3.0 * x[i] + 0.3 * self.dim)
            saddle = well1 + well2
            # Dynamic basin modulation with fractal scaling and adaptive coupling
            basin_mod = 1.0 + 0.4 * np.sin(0.5 * x[i] + self.dim * 0.4 + 0.2 * np.cos(x[i]))
            chaotic += basin_mod * saddle
        
        # Enhanced non-separability through multi-scale fractal coupling
        coupling = 0
        for i in range(self.dim):
            # Multi-scale coupling with exponential decay and dynamic weights
            for j in range(max(0, i-2), min(i+3, self.dim)):
                if i != j:
                    # Fractal coupling strength with time-varying parameters
                    coupling_strength = 2.0 * np.exp(-0.15 * (i - j)**2) * (1.0 + 0.3 * np.sin(0.3 * x[i] + 0.4 * x[j] + 0.1 * self.dim))
                    distance = np.abs(x[i] - x[j])
                    coupling_factor = 1.0 / (1.0 + np.exp(3.0 * distance))
                    coupling += coupling_strength * coupling_factor * (x[i]**2 + x[j]**2)
        
        # Dynamic ridge structures with chaotic modulation and multi-scale interference
        ridges = 0
        for i in range(self.dim):
            # Chaotic ridge height, width, and phase modulation
            height = 2.0 + 1.0 * np.sin(0.7 * x[i] + self.dim * 0.3 + 0.5 * np.cos(x[i]))
            width = 1.0 + 0.5 * np.cos(0.6 * x[i] + 0.2 * self.dim + 0.3 * np.sin(x[i]))
            # Saddle point ridge with chaotic phase interference
            phase = np.sin(0.8 * x[i] + self.dim * 0.5 + 0.4 * np.cos(x[i]))
            ridge = height * np.exp(-0.5 * ((x[i] - 1.0) / width)**2) * (1.0 + 0.4 * phase)
            ridges += ridge
        
        # Multi-scale oscillatory components with quantum tunneling and fractal frequency modulation
        oscillatory = 0
        for i in range(self.dim):
            # Fractal frequency modulation with multiple scales and chaotic phase shifts
            freq1 = 2.5 + 1.5 * np.sin(0.4 * x[i] + 0.1 * self.dim)
            freq2 = 3.5 + 2.0 * np.cos(0.5 * x[i] + 0.2 * self.dim + 0.1 * np.sin(x[i]))
            freq3 = 4.5 + 2.5 * np.sin(0.6 * x[i] + 0.3 * self.dim + 0.2 * np.cos(x[i]))
            # Quantum tunneling effect with dynamic probability and chaotic modulation
            tunneling_prob = 0.6 + 0.4 * np.sin(0.7 * x[i] + 0.1 * self.dim)
            oscillatory += (np.sin(freq1 * x[i]) * 
                           np.cos(freq2 * x[i]**2) * 
                           np.sin(freq3 * x[i]**3) * 
                           tunneling_prob * 
                           np.exp(-0.2 * x[i]**2))
        
        # Asymmetric multimodal with chaotic phase interference and enhanced ridge coupling
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 1.5)**2) * np.sin(5.0 * x[i] + 0.3 * self.dim)
            term2 = np.exp(-0.5 * (x[i] + 1.5)**2) * np.cos(4.0 * x[i] + 0.2 * self.dim)
            term3 = np.exp(-0.3 * x[i]**2) * np.sin(6.0 * x[i]**2 + 0.1 * self.dim)
            # Chaotic phase interference with dynamic scaling
            phase_interference = np.sin(0.9 * x[i] + self.dim * 0.3 + 0.2 * np.cos(x[i]))
            asymmetric += (term1 + term2 + term3) * (1.0 + 0.5 * phase_interference)
        
        # Dynamic conditioning with chaotic scaling and multi-scale modulation
        condition = 2.0 + 0.8 * np.sin(0.6 * x[0] + self.dim * 0.25 + 0.3 * np.cos(x[0]))
        
        # Combine all components with increased complexity weights
        return condition * (0.30 * chaotic + 0.25 * coupling + 
                           0.20 * ridges + 0.20 * oscillatory + 0.05 * asymmetric)