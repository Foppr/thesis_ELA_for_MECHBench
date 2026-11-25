import numpy as np

class ChaoticHypercubeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic component with logistic map dynamics and embedded saddle points
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with parameter modulation and saddle point insertion
            r = 3.9 + 0.1 * np.sin(x_scaled[i] * 2.0)
            x_next = r * x_scaled[i] * (1.0 - x_scaled[i])
            chaotic += x_next**2 + 0.1 * np.sin(10.0 * x_scaled[i]) * np.cos(5.0 * x_scaled[i])
        
        # Multi-scale periodicity with asymmetric harmonics and phase shifts
        periodic = 0.0
        for i in range(self.dim):
            # Multiple harmonic components with varying frequencies and amplitudes
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            amps = [1.0, 0.8, 0.6, 0.4, 0.2]
            phases = [0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
            
            for freq, amp, phase in zip(freqs, amps, phases):
                periodic += amp * np.sin(freq * x_scaled[i] + phase) * \
                           np.cos(freq * x_scaled[i] + phase) * \
                           np.exp(-0.5 * (x_scaled[i] - 0.5)**2)
        
        # Asymmetric gradient flow with directional bias and multi-modal peaks
        gradient = 0.0
        for i in range(self.dim):
            # Directional bias with asymmetric exponential terms
            bias = 0.5 + 0.3 * np.sin(x_scaled[i] * 3.0)
            gradient += (x_scaled[i]**2) * np.exp(-bias * x_scaled[i]**2) + \
                       0.3 * np.sin(2.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[i])
        
        # Embedded saddle points with higher-order polynomial interactions
        saddles = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Saddle point configuration with mixed positive/negative curvature
                term = (x_scaled[i]**2 - x_scaled[j]**2) * np.exp(-0.5 * (x_scaled[i] + x_scaled[j])**2)
                saddles += term * (1.0 + 0.2 * np.sin(i + j))
        
        # Combined landscape with modified weights and interaction terms
        return 1.2 * chaotic + 0.8 * periodic + 0.6 * gradient + 0.4 * saddles