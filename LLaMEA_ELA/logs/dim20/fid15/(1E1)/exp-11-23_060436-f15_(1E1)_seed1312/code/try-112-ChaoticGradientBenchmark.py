import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component with modified conditioning
        quadratic = np.sum(x**2) * 0.15
        
        # Enhanced chaotic gradient component with higher frequency modulation
        chaotic_grad = 0
        for i in range(self.dim):
            freq1 = 3.0 + 0.7 * np.sin(i * 0.8)
            freq2 = 2.8 + 0.6 * np.cos(i * 0.6)
            freq3 = 2.2 + 0.5 * np.sin(0.4 * i)
            
            term1 = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.4 * x[i]**2)
            term2 = np.cos(freq3 * x[i]) * np.sin(freq1 * x[i]) * np.exp(-0.25 * (x[i] - 1.8)**2)
            term3 = np.sin(freq2 * x[i]) * np.cos(freq3 * x[i]) * np.exp(-0.35 * (x[i] + 1.5)**2)
            
            chaotic_grad += (term1 + term2 + term3) * (1.0 + 0.3 * np.sin(0.4 * i))
        
        # Enhanced saddle point component with stronger curvature variation
        saddle = 0
        for i in range(self.dim):
            saddle_loc = 2.5 * np.sin(i * 0.6)
            condition_factor = 1.0 + 0.7 * np.cos(i * 0.4)
            
            saddle_term = (x[i] - saddle_loc)**2 * (x[i] - saddle_loc)**5 * condition_factor
            saddle += saddle_term
        
        # Enhanced multi-scale oscillatory component with additional frequencies
        oscillatory = 0
        scales = [0.3, 0.7, 1.2, 2.5, 3.8]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            
            osc_term = np.sin(scale * x[i]) * np.cos(1.8 * scale * x[i]) * np.exp(-0.12 * (x[i] - 1.5)**2)
            osc_term += np.cos(scale * x[i]) * np.sin(2.2 * scale * x[i]) * np.exp(-0.18 * (x[i] + 1.8)**2)
            osc_term += np.sin(2.0 * scale * x[i]) * np.cos(0.8 * scale * x[i]) * np.exp(-0.08 * x[i]**2)
            
            oscillatory += osc_term * (1.0 + 0.15 * np.sin(i * 0.5))
        
        # Enhanced cross-dimensional interaction with increased complexity
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended interaction range
                weight = 0.7 + 0.3 * np.sin(0.25 * (i + j))
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Enhanced variable dimension coupling with dynamic scaling
        coupling = 0
        for i in range(self.dim):
            coupling_factor = 1.0 + 0.4 * np.sin(0.5 * i)
            coupling += (np.sin(x[i] * coupling_factor) * np.cos(x[i] * coupling_factor) * 
                        np.exp(-0.25 * x[i]**2) * coupling_factor)
        
        # Enhanced asymmetric chaotic modulation
        asymmetric = 0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.4 * np.sin(0.35 * i)
            asym_term = (np.sin(x[i] * asym_factor) * np.exp(-0.12 * x[i]**2) + 
                        np.cos(x[i] * asym_factor) * np.exp(-0.18 * x[i]**2))
            asymmetric += asym_term
        
        # Enhanced hybrid polynomial-chaotic with memory and higher-order terms
        memory = 0
        for i in range(self.dim):
            memory += (np.sin(x[i]**4) * np.cos(x[i]) * np.exp(-0.12 * (x[i] - 1.2)**2) + 
                      np.cos(x[i]**3) * np.sin(x[i]) * np.exp(-0.18 * (x[i] + 1.2)**2) +
                      np.sin(x[i]**2) * np.cos(x[i]**3) * np.exp(-0.15 * x[i]**2))
        
        # Additional component: Nonlinear coupling with exponential decay
        nonlinear = 0
        for i in range(self.dim):
            nonlinear += (np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(3.0 * x[i]) + 
                         np.exp(-0.15 * (x[i] + 2.0)**2) * np.cos(2.5 * x[i]))
        
        # Additional component: Multi-modal Gaussian mixture with varying peaks
        gaussian = 0
        peaks = [(-3.0, 0.8), (-1.0, 0.6), (0.0, 1.0), (1.0, 0.7), (3.0, 0.9)]
        for i in range(self.dim):
            for peak_x, amplitude in peaks:
                gaussian += amplitude * np.exp(-0.5 * ((x[i] - peak_x) / 0.8)**2)
        
        # Combine all components with optimized weights
        return (quadratic * 0.9 +
                chaotic_grad * 0.55 +
                saddle * 0.45 +
                oscillatory * 0.65 +
                interaction * 0.35 +  
                coupling * 0.20 +
                asymmetric * 0.30 +   
                memory * 0.22 +
                nonlinear * 0.18 +
                gaussian * 0.15)