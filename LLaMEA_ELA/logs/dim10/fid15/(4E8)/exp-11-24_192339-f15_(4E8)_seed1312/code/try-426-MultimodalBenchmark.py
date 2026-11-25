import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic saddle point dynamics with quantum coupling
        chaotic = 0
        for i in range(self.dim):
            well1 = np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(4.0 * x[i])
            well2 = np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(3.0 * x[i])
            quantum_phase = np.exp(1j * (0.3 * x[i] + self.dim * 0.4))
            phase_mod = 1.0 + 0.5 * np.sin(0.3 * x[i] + self.dim * 0.4)
            saddle = (well1 + well2) * phase_mod * np.real(quantum_phase)
            chaotic += saddle
        
        # Fractal ridge coupling with adaptive scaling and interference
        coupling = 0
        for i in range(self.dim):
            for j in range(max(0, i-3), min(i+4, self.dim)):
                if i != j:
                    coupling_strength = 1.5 * np.exp(-0.2 * (i - j)**2) * (1.0 + 0.4 * np.sin(0.4 * x[i] + 0.5 * x[j]))
                    distance = np.abs(x[i] - x[j])
                    coupling_factor = 1.0 / (1.0 + np.exp(2.0 * distance))
                    ridge_mod = 1.0 + 0.5 * np.cos(0.7 * x[i] + 0.4 * self.dim)
                    coupling += coupling_strength * coupling_factor * (x[i]**2 + x[j]**2) * ridge_mod
        
        # Quantum-inspired oscillatory components with dynamic tunneling and phase shifts
        oscillatory = 0
        for i in range(self.dim):
            freq1 = 3.0 + 2.0 * np.sin(0.5 * x[i])
            freq2 = 4.0 + 2.5 * np.cos(0.6 * x[i] + 0.2 * self.dim)
            freq3 = 5.0 + 3.0 * np.sin(0.7 * x[i] + 0.3 * self.dim)
            tunneling_prob = 0.7 + 0.3 * np.sin(0.8 * x[i] + self.dim * 0.2)
            phase_shift = np.exp(1j * (0.9 * x[i] + 0.1 * self.dim))
            oscillatory += (np.sin(freq1 * x[i]) * 
                           np.cos(freq2 * x[i]**2) * 
                           np.sin(freq3 * x[i]**3) * 
                           tunneling_prob * 
                           np.exp(-0.25 * x[i]**2) * 
                           np.real(phase_shift))
        
        # Asymmetric multimodal with enhanced chaotic interference and fractal modulation
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 1.5)**2) * np.sin(6.0 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 1.5)**2) * np.cos(5.0 * x[i])
            term3 = np.exp(-0.4 * x[i]**2) * np.sin(7.0 * x[i]**2)
            fractal_mod = 1.0 + 0.6 * np.sin(0.8 * x[i] + self.dim * 0.5)
            phase_interference = np.sin(1.2 * x[i] + self.dim * 0.4)
            asymmetric += (term1 + term2 + term3) * fractal_mod * (1.0 + 0.6 * phase_interference)
        
        # Dynamic conditioning with enhanced chaotic scaling factor and multi-modal modulation
        condition = 2.5 + 1.2 * np.sin(0.8 * x[0] + self.dim * 0.35)
        
        # Combine all components with optimized weights for improved performance
        return condition * (0.35 * chaotic + 0.28 * coupling + 
                           0.22 * oscillatory + 0.15 * asymmetric)